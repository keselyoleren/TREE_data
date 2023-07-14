from rest_framework import serializers
from app.models import Orang
from rest_framework_recursive.fields import RecursiveField

class ParentSerialize(serializers.ModelSerializer):
    class Meta:
        model = Orang
        fields = ['nama', 'jenis_kelamin']


class OrangSerialize(serializers.ModelSerializer):
    nama = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    jenis_kelamin = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    children = serializers.ListSerializer(read_only=True, child=RecursiveField())

    
    class Meta:
        model = Orang
        fields = ('id', 'nama', 'jenis_kelamin', 'children')

def generate_password():
    pass

def edit_proses():
    pass

def generate_data():
    data = [
        {
            "id": 1,
            "nama": "Budi",
            "jenis_kelamin": "Laki-laki",
            "children": [
                {
                    "id": 2,
                    "nama": "Bambang",
                    "jenis_kelamin": "Laki-laki",
                    "children": [
                        {
                            "id": 3,
                            "nama": "Bambang",
                            "jenis_kelamin": "Laki-laki",
                            "children": []
                        }
                    ]
                },
                {
                    "id": 4,
                    "nama": "Bambang",
                    "jenis_kelamin": "Laki-laki",
                    "children": []
                }
            ]
        },
        {
            "id": 5,
            "nama": "Bambang",
            "jenis_kelamin": "Laki-laki",
            "children": []
        }
    ]
    return data