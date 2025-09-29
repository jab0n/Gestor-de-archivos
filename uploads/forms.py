from django import forms

class MultipleFileUploadForm(forms.Form):
    archivos = forms.FileField(
        widget=forms.ClearableFileInput(),
        required=True,
    )

    def clean_archivos(self):
        archivos = self.files.getlist("archivos")
        extensiones_permitidas = [".jpg", ".jpeg", ".png", ".gif", ".pdf"]

        for archivo in archivos:
            nombre = archivo.name.lower()
            if not any(nombre.endswith(ext) for ext in extensiones_permitidas):
                raise forms.ValidationError(
                    f"El archivo '{archivo.name}' no es una imagen ni un PDF válido."
                )

        return archivos