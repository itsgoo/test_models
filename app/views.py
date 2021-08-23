from django.shortcuts import render
from django.views.generic.base import View
from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.

class MainForm(View):
	def get(self, request):
		form = CustomUserCreationForm
		users = CustomUser.objects.all()
		ctx = {
			'users': users,
			'form': form,
		}
		return render(request, 'index.html', ctx)

	# def post(self, request):
	# 	req = request.POST
	# 	list_form = CustomUserCreationForm(req)
	# 	if list_form.is_valid():
	# 		add_list_element = list_form.save(commit=True)
	# 		add_list_element.username = req.get('column_name')
	# 		add_list_element.column_type = req.get('column_type')
	# 		add_list_element.parameters = req.get('parameters')
	# 		add_list_element.order = req.get('order') 
	# 		add_list_element.schema_id = get_object_or_404(Schema, id=pk)

	# 		if add_list_element.schema_id.author != request.user:
	# 			return HttpResponseForbidden()
	# 		add_list_element.save()
	# 		return HttpResponseRedirect(self.request.path_info)