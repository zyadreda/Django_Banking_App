from django.contrib import admin
from .models import Investment_Approval, Loan_Funding_Option, Invest_in_Loan_Fund, Total, Loan_option, Loan_Request, Loan_approval
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin 
from django.contrib.contenttypes.models import ContentType

admin.site.register(Loan_Funding_Option)
admin.site.register(Invest_in_Loan_Fund)
admin.site.register(Total)
admin.site.register(Loan_option)
admin.site.register(Loan_Request)
admin.site.register(Loan_approval)
admin.site.register(Investment_Approval)

if (Total.objects.all().count()==0):
    Total.objects.create()

admin.site.unregister(User) 

@admin.register(User) 
class NewAdmin(UserAdmin): 
    readonly_fields = [ 
        'date_joined', 
    ] 

    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True 

        return form 