from django.db import models

z = [('Check Loan Fund First', 'Check Loan Funding Options First')]

class Loan_Funding_Option(models.Model):
    name = models.CharField(max_length=200, default=None)
    Minimum_Amount = models.IntegerField()
    Maximum_Amount = models.IntegerField()
    Interest_Rate = models.IntegerField()
    Duration_in_Days = models.IntegerField()
    def __str__(self):
        z.clear()
        for val in Loan_Funding_Option.objects.all():
            z.append((val.name, val.name))
        return self.name + " with a Minimum investment of " + str(self.Minimum_Amount) + " EGP, a Maximum investment of " + str(self.Maximum_Amount) + "EGP, and an Interest rate of " + str(self.Interest_Rate) + "%, for a duration of " + str(self.Duration_in_Days) + " days!"

class Investment_Approval(models.Model):
    full_name = models.CharField(max_length=200, help_text="Enter Your Full Name", default=None)
    Name_of_Fund = models.CharField(max_length=200, choices=z, help_text="Only choose when you have looked at the Investment Options", default=None)
    Amount = models.IntegerField(default=None)
    date_of_deposit = models.DateTimeField(auto_now=True)
    Deposit_Confirmation = models.CharField(max_length=200, choices={("pending","Pending"), ("confirm", "Approve"), ("reject", "Reject")}, default="pending")
    Comments = models.TextField(max_length=2000, default="", blank=True, help_text="If Rejected, Write reason of Rejection")
    def __str__(self):
        return self.full_name + " wants to invest " + str(self.Amount) + " EGP in the " + self.Name_of_Fund + " on " + str(self.date_of_deposit) + ". Status: " + self.Deposit_Confirmation
    

class Invest_in_Loan_Fund(models.Model):
    full_name = models.CharField(max_length=200, help_text="Enter Your Full Name", default=None)
    Name_of_Fund = models.CharField(max_length=200, choices=z, help_text="Only choose when you have looked at the Investments Options", default=None)
    Amount = models.IntegerField(default=None)
    date_of_deposit = models.DateTimeField(auto_now=True)
    def __str__(self):
        for x in Invest_in_Loan_Fund.objects.all():
             #print(x.Full_name)
             y = Investment_Approval.objects.filter(full_name=x.full_name)
             if (y.count()==0):
                #print(y.count())
                Investment_Approval.objects.create(full_name=x.full_name, Name_of_Fund=x.Name_of_Fund, Amount=x.Amount, date_of_deposit=x.date_of_deposit, Deposit_Confirmation="pending") 
        investment = Investment_Approval.objects.filter(full_name = self.full_name)
        status = ""
        for x in investment.all():
            if x.Deposit_Confirmation == "confirm":
                status = "Confirmed!"
            elif x.Deposit_Confirmation == "pending":
                status = "Pending"
            else:
                status = "Rejected, " + x.Comments
        return self.full_name + " invested " + str(self.Amount) + " EGP in the " + str(self.Name_of_Fund) + " on " +str(self.date_of_deposit) + " Deposit Status: " + status


class Total(models.Model):
    Total_funding = models.IntegerField()
    def __str__(self):
        Total_funds = 0
        for val in Loan_approval.objects.all():
            Total_funds = Total_funds + val.Amount
        for val in Total.objects.all():
            val.Total_funding = Total_funds
            val.save()
            print(val.Total_funding)
        return "Total Funding: " + str(Total_funds) + " EGP"
    

x = [('Check Loan Options First', 'Check Loan Options First')]

class Loan_option(models.Model):
    type_of_loan = models.CharField(max_length=200)
    Minimum_Amount = models.IntegerField()
    Maximum_Amount = models.IntegerField()
    Interest_Rate = models.IntegerField()
    Duration_in_Days = models.IntegerField()
    def __str__(self):
        x.clear()
        for val in Loan_option.objects.all():
            x.append((val.type_of_loan, val.type_of_loan))
        return self.type_of_loan + " with a minimum amount of " + str(self.Minimum_Amount) + " EGP and a maximum amount of " + str(self.Maximum_Amount) + " EGP and an interest rate of " + str(self.Interest_Rate) + " Percent for a duration of " + str(self.Duration_in_Days) + " days!"

class Loan_approval(models.Model):
    Full_name = models.CharField(max_length=200, help_text="Enter Your Full Name", default=None)
    type_of_loan = models.CharField(max_length=200, choices=x, help_text="Only choose when you have looked at the Loan Options First", default=None)
    Amount = models.IntegerField(default=None)
    date_of_request = models.DateTimeField(auto_now=True)
    Approval = models.CharField(max_length=200, choices={("pending","Pending"), ("approve", "Approve"), ("reject", "Reject")}, default="pending")
    Comments = models.TextField(max_length=2000, default="", blank=True, help_text="Reason of Rejection")
    def __str__(self):
        return self.Full_name + " requested a " + self.type_of_loan + " of " + str(self.Amount) + " EGP. Status: " + self.Approval 

class Loan_Request(models.Model):
    Full_name = models.CharField(max_length=200, help_text="Enter Your Full Name", default=None)
    type_of_loan = models.CharField(max_length=200, choices=x, help_text="Only choose when you have looked at the Loan Options First", default=None)
    Amount = models.IntegerField(default=None)
    date_of_request = models.DateTimeField(auto_now=True)
    def __str__(self):
        for x in Loan_Request.objects.all():
             #print(x.Full_name)
             y = Loan_approval.objects.filter(Full_name=x.Full_name)
             if (y.count()==0):
                #print(y.count())
                Loan_approval.objects.create(Full_name=x.Full_name, type_of_loan=x.type_of_loan, Amount=x.Amount, date_of_request=x.date_of_request, Approval="pending")
        Total_money = 0
        for val in Total.objects.all():
            Total_money = Total_money + val.Total_funding
            print(val.Total_funding)
        Total_Loans = 0
        for val in Loan_Request.objects.all():
            Total_Loans = Total_Loans + val.Amount
            #print(Total_Loans)
        if Total_money >= Total_Loans:
            loan = Loan_approval.objects.filter(Full_name = self.Full_name)
            for x in loan.all():
                if x.Approval == "approve":
                    return self.Full_name + " requested a " + self.type_of_loan + " of " + str(self.Amount) + " EGP. Status: Loan Approved!"
                elif x.Approval == "reject":
                    return self.Full_name + " requested a " + self.type_of_loan + " of " + str(self.Amount) + " EGP. Status: Loan rejected, " + x.Comments 
                else:
                    return "Loan waiting for Confirmation" 
        else:
            return self.Full_name + " requested a " + self.type_of_loan + " of " + str(self.Amount) + " EGP. Status: Loan rejected, try a smalller amount"                  
                   
