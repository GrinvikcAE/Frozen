from rest_framework import serializers


class FilterCommentListSerializer(serializers.ListSerializer):
    """Filter to comments, only parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Recursive method to export children """
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
