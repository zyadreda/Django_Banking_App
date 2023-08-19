from django.test import TestCase
from datetime import datetime
from .models import Invest_in_Loan_Fund as Invest_in_Loan_FundModel, Investment_Approval as Investment_ApprovalModel, Loan_Funding_Option as Loan_Funding_OptionModel, Loan_Request as Loan_RequestModel, Loan_approval as Loan_approvalModel, Loan_option as Loan_optionModel

# Create your tests here.

class Investment_Approval(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.investment_Approval = Investment_ApprovalModel.objects.create(
            full_name ="testing_Loan_funding_options", 
            Name_of_Fund = "test_name",
            Amount=1000, 
            date_of_deposit=2023-8-12, 
            Deposit_Confirmation = 'confirm', 
            Comments = 'Test_comment'
            )

    def test_fields(self):
        
        self.assertIsInstance(self.investment_Approval.full_name, str)

        self.assertIsInstance(self.investment_Approval.Name_of_Fund, str)

        self.assertIsInstance(self.investment_Approval.Amount, int)

        self.assertIsInstance(self.investment_Approval.date_of_deposit, datetime)

        self.assertIsInstance(self.investment_Approval.Deposit_Confirmation, str)

        self.assertIsInstance(self.investment_Approval.Comments, str)

class Invest_in_Loan_Fund(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.invest_in_Loan_Fund = Invest_in_Loan_FundModel.objects.create(
            full_name ="testing_Loan_funding_options", 
            Name_of_Fund = "test_name",
            Amount=1000, 
            date_of_deposit=2023-8-12, 
            )

    def test_fields(self):
        
        self.assertIsInstance(self.invest_in_Loan_Fund.full_name, str)

        self.assertIsInstance(self.invest_in_Loan_Fund.Name_of_Fund, str)

        self.assertIsInstance(self.invest_in_Loan_Fund.Amount, int)

        self.assertIsInstance(self.invest_in_Loan_Fund.date_of_deposit, datetime)



class Loan_Funding_Option(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.loan_Funding_Option = Loan_Funding_OptionModel.objects.create(
            name ="test", 
            Minimum_Amount = 10,
            Maximum_Amount=1000, 
            Interest_Rate=10, 
            Duration_in_Days = 10, 
            )

    def test_fields(self):
        
        self.assertIsInstance(self.loan_Funding_Option.name, str)

        self.assertIsInstance(self.loan_Funding_Option.Minimum_Amount, int)

        self.assertIsInstance(self.loan_Funding_Option.Maximum_Amount, int)

        self.assertIsInstance(self.loan_Funding_Option.Interest_Rate, int)

        self.assertIsInstance(self.loan_Funding_Option.Duration_in_Days, int)


class Loan_Request(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.loan_Request = Loan_RequestModel.objects.create(
            Full_name ="test", 
            type_of_loan = "short_term",
            Amount=1000, 
            date_of_request=2023-10-10, 
    
            )

    def test_fields(self):
        
        self.assertIsInstance(self.loan_Request.Full_name, str)

        self.assertIsInstance(self.loan_Request.type_of_loan, str)

        self.assertIsInstance(self.loan_Request.Amount, int)

        self.assertIsInstance(self.loan_Request.date_of_request, datetime)


class Loan_approval(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.loan_approval = Loan_approvalModel.objects.create(
            Full_name ="test", 
            type_of_loan = "short_term",
            Amount=1000, 
            date_of_request=2023-10-10, 
            Approval = 'pending',
            Comments = 'test',
            )

    def test_fields(self):
        
        self.assertIsInstance(self.loan_approval.Full_name, str)

        self.assertIsInstance(self.loan_approval.type_of_loan, str)

        self.assertIsInstance(self.loan_approval.Amount, int)

        self.assertIsInstance(self.loan_approval.date_of_request, datetime)

        self.assertIsInstance(self.loan_approval.Approval, str)

        self.assertIsInstance(self.loan_approval.Comments, str)


class Loan_option(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.loan_option = Loan_optionModel.objects.create(
            type_of_loan = "short_term",
            Minimum_Amount=1000, 
            Maximum_Amount=1000, 
            Interest_Rate = 10,
            Duration_in_Days=20, 
            )

    def test_fields(self):

        self.assertIsInstance(self.loan_option.type_of_loan, str)

        self.assertIsInstance(self.loan_option.Minimum_Amount, int)

        self.assertIsInstance(self.loan_option.Maximum_Amount, int)

        self.assertIsInstance(self.loan_option.Interest_Rate, int)

        self.assertIsInstance(self.loan_option.Duration_in_Days, int)
