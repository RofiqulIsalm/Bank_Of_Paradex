from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type']
        
    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account') # problem in this line 
        super.__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput
        
    def save(self, commit = True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()
        

class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )
        return amount

class WithdrawForm(TransactionForm):
    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 100
        max_withdrwa_amout = 20000
        balance = account.balance
        amount = self.cleaned_data.get('amount')
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at last {min_withdraw_amount} $'
            )
        
        if amount > max_withdrwa_amout:
            raise forms.ValidationError(
                f'You  can withdraw at most {max_withdrwa_amout} $'
            )
        if amount > balance:
            raise forms.ValidationError(
                f'You have {balance} $ in your account',
                'You can not  withdraw more then your account balance'
            )
        return amount
    
class LoanRequestForms(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        
        # You can add here your loan condition 
        
        return amount