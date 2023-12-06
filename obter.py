from django.db.models import ForeignKey, ManyToManyField
from local.models import Local

def obter_referencias(modelo):
    referencias = []

    for campo in modelo._meta.get_fields():
        if isinstance(campo, (ForeignKey, ManyToManyField)):
            referencias.append({
                'campo': campo,
                'modelo_referenciado': campo.related_model,
            })

    return referencias

# Exemplo de uso para o modelo Local
referencias_a_local = obter_referencias(Local)

for referencia in referencias_a_local:
    print(f"Campo: {referencia['campo'].name}")
    print(f"Modelo Referenciado: {referencia['modelo_referenciado'].__name__}")
    print()
