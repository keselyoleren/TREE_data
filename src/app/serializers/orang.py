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

def generate_data():
    data = [
        {
            "id": 1,
            "nama": "A",
            "jenis_kelamin": "L",
            "children": [
                {
                    "id": 2,
                    "nama": "B",
                    "jenis_kelamin": "L",
                    "children": [
                        {
                            "id": 3,
                            "nama": "C",
                            "jenis_kelamin": "L",
                            "children": []
                        },
                        {
                            "id": 4,
                            "nama": "D",
                            "jenis_kelamin": "P",
                            "children": []
                        }
                    ]
                },
                {
                    "id": 5,
                    "nama": "E",
                    "jenis_kelamin": "P",
                    "children": [
                        {
                            "id": 6,
                            "nama": "F",
                            "jenis_kelamin": "L",
                            "children": []
                        },
                        {
                            "id": 7,
                            "nama": "G",
                            "jenis_kelamin": "P",
                            "children": []
                        }
                    ]
                }
            ]
        }
    ]
    return data