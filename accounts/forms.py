# accounts/forms.py
from django import forms

#入学者一括登録フォーム
class StudentBatchCreateForm(forms.Form):
    year = forms.IntegerField(label="入学年度", min_value=2000, max_value=2100)
    department = forms.ChoiceField(label="学科", choices=[('42', '経営学科'), ('41', '経済学科')])
    count = forms.IntegerField(label="作成人数", min_value=1, max_value=100)
    prefix = forms.ChoiceField(label="種別", choices=[('A', '入学者'), ('R', '再入学者')])
