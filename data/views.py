from django.shortcuts import render, redirect
from django.views import View
from .forms import StepOneForm, StepTwoForm, StepThreeForm
from data.models import FormData
class StepOneView(View):
    def get(self, request):
        form = StepOneForm()
        return render(request, 'step_one.html', {'form': form})

    def post(self, request):
        form = StepOneForm(request.POST)
        if form.is_valid():
            request.session['step_one_data'] = form.cleaned_data
            print(request.session.get('step_one_data', {}))
            return redirect('step_two')
        return render(request, 'step_one.html', {'form': form})

class StepTwoView(View):
    def get(self, request):
        form = StepTwoForm()
        return render(request, 'step_two.html', {'form': form})

    def post(self, request):
        form = StepTwoForm(request.POST)
        if form.is_valid():
            request.session['step_two_data'] = form.cleaned_data
            return redirect('step_three')
        return render(request, 'step_two.html', {'form': form})

class StepThreeView(View):
    def get(self, request):
        form = StepThreeForm()
        return render(request, 'step_three.html', {'form': form})

    def post(self, request):
        form = StepThreeForm(request.POST)
        if form.is_valid():
            request.session['step_three_data'] = form.cleaned_data
            return redirect('summary')
        return render(request, 'step_three.html', {'form': form})

class SummaryView(View):
    def get(self, request):
        step_one_data = request.session.get('step_one_data', {})
        step_two_data = request.session.get('step_two_data', {})
        step_three_data = request.session.get('step_three_data', {})
        data = {**step_one_data, **step_two_data, **step_three_data}
        form_data = FormData(**data)
        
        form_data.save()
        request.session.clear()

        return render(request, 'summary.html', {'data': data})
