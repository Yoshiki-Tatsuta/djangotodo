from django import forms


class TranslationForm(forms.Form):
    trans_ja = forms.CharField(label="翻訳（日本語）", widget=forms.Textarea(), required=True)
    trans_en = forms.CharField(label="翻訳（英語）", widget=forms.Textarea())