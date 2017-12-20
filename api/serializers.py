from rest_framework import serializers

from hello.models import Animal


class APISerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.CharField(read_only=True, source='user.username')

    class Meta:
        model = Animal
        fields = ('name', 'birthday', 'type', 'user')
        extra_kwargs = {
            'url': {
                'view_name': 'apis:api-detail',
            }
}