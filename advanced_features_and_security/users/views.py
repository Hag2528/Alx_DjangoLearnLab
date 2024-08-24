from django.shortcuts import render,redirect
from django.contrib.auth.decorators import permission_required


@permission_required('app_name.view_mymodel', raise_exception=True)
def view_mymodel(request, pk):
    # Fetch MyModel instance
    mymodel = MyModel.objects.get(pk=pk)
    # ... (process and display MyModel data)
    return render(request, 'view_mymodel.html', {'mymodel': mymodel})

@permission_required('app_name.create_mymodel', raise_exception=True)
def create_mymodel(request):
    if request.method == 'POST':
        # ... (validate and save new MyModel instance)
        return redirect('success_url')  # Replace with appropriate redirect URL
    # ... (display form for creating MyModel)
    return render(request, 'create_mymodel.html')