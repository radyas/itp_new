from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'id', 'name']


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.CharField(write_only=True)
    # user_groups = serializers.ListField(write_only=True)

    class Meta:
        model = Employee
        fields = [
            'url', 'username', 'email', 'groups', 'first_name', 'last_name', 'address', 'dob', 'nic', 'phone',
            'department', 'department_id', 'id'
        ]

    def create(self, validated_data):
        # group_list = validated_data.pop('user_groups')
        # groups = Group.objects.all()
        user = Employee.objects.create(**validated_data)
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.set_password("user@123")
        user.save()
        # for group_data in group_list:
        #     group = groups.filter(pk=group_data).get()
        #     user.groups.add(group)
        return user


class CustomersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomersSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class DeliverySerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    provider = ProviderSerializer(read_only=True)

    class Meta:
        model = Delivery
        fields = "__all__"


class VoucherSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Voucher
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = "__all__"


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = "__all__"


class AdjustmentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adjustments
        fields = "__all__"


class DocumentsSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Documents
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"
