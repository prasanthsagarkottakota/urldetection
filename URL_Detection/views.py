# views.py
from django.http import HttpResponse
from django.shortcuts import render
import joblib
from scripts import Functions
#import sys
#sys.path.append('/path/to/functions_directory')

# views.py
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        input_value = request.POST.get('inputValue')
        
        # If input value is empty, set it to "No URL"
        if not input_value:
            input_value = "No URL"
            output_value = "NOT ACCESSIBLE"
        else:
            classifier = joblib.load('RandomForestClassifier.joblib')
            if Functions.check_url_accessibility(input_value):
                output_value = Functions.model_predict1(classifier, input_value)
            else:
                output_value = "NOT ACCESSIBLE"
        
        return render(request, 'index.html', {'input_value': input_value, 'output_value': output_value})
    
    return render(request, 'index.html')
