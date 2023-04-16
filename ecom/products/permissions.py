from rest_framework.permissions import BasePermission, SAFE_METHODS

class ProductPermission(BasePermission):
    
    """
    Roles:
        Staff:
            View: ProductAV
            Allowed:
                -   Create Products
                -   Delete Product
                -   Update Product
        Customer:
            View: ProductAV
            Allowed:
                -   Retrieve Products
    """
    
    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            if request.user.is_anonymous:
                print("Anon User...")
                return False
            if request.user.role != "ST":
                return False
        return True