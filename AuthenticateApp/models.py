from typing import Any
from django.db import models
from django.db.models import Q
# from . models import Employee, Expense, Reimbursment, Approval, Status

# Employee Model/Table
class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=20, null=False)
    LastName = models.CharField(max_length=20, null=False)
    EmailID = models.EmailField(null=False)
    MobileNo = models.CharField(max_length=15, null=False)
    Designation = models.CharField(max_length=20, null=False)

    # Department field with ForeignKey
    Department = models.ForeignKey('Department', on_delete=models.CASCADE, null=False)

    # Role field with a check constraint
    ROLE_CHOICES = (
        ('Trainee', 'Trainee'),
        ('Associate', 'Associate'),
        ('Consultant', 'Consultant'),
        ('Senior Associate', 'Senior Associate'),
        ('Manager', 'Manager'),
    )
    Role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        null=False,
    )

    class Meta:
        constraints=[
            models.CheckConstraint(
                check=models.Q(Role__in=['Trainee', 'Associate', 'Consultant', 'Senior Associate','Manager']),
                name='valid_role_check',
            )
        ]




    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
    
# Expense Model/Table
class Expense(models.Model):
    ExpenseID = models.AutoField(primary_key=True)
    EmployeeID = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE, 
        null=False, 
        related_name='expenses_submitted'  # Unique related_name for expenses submitted by the employee
        )  
    
    ExpenseDate = models.DateField(null=False)
    #ExpenseType = models.ForeignKey('Reimbursment', on_delete=models.CASCADE, null=False)

    # Role field with a check constraint
    EXPENSETYPE_CHOICES = (
        ('Travel', 'Travel'),
        ('Suppplies', 'Suppplies'),
        ('Training', 'Training'),
        ('Services', 'Services'),
    )
    ExpenseType = models.CharField(
        max_length=20,
        choices=EXPENSETYPE_CHOICES,
        null=False,
    )

    class Meta:
        constraints=[
            models.CheckConstraint(
                check=models.Q(ExpenseType__in=['Travel', 'Suppplies', 'Training', 'Services']),
                name='valid_expensetype_check',
            )
        ]


    Detail = models.CharField(max_length=250, null=False)
    Amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    STATUS_CHOICES = (
        ('Created', 'Created'),
        ('In Process', 'In Process'),
        ('Verified', 'Verified'),
        ('Rejected', 'Rejected'),
        ('Disputed', 'Disputed'),
    )
    Status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        null=False,
    )

    class Meta:
        constraints=[
            models.CheckConstraint(
                check=models.Q(Status__in=['Created', 'In Process', 'Verified', 'Rejected','Disputed']),
                name='valid_status_check',
            )
        ]
        
    ApproverID = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE, 
        null=False,
        related_name='expenses_approved', # Unique related_name for expenses approved by the employee
        # limit_choices_to=Q(Role='Manager') & Q(EmployeeID__Department=models.F('EmployeeID__Department'))
        # limit_choices_to=Q(Role='Manager') & Q(Department=models.F('EmployeeID__Department'))
        limit_choices_to={'Role': 'Manager'}  # Limit choices to employees with Role 'Manager'
        ) 

    Comments = models.TextField(max_length=250, null=False)

    def __str__(self):
        return f"Expense #{self.ExpenseID} by {self.EmployeeID}"




# Department Model/Table
class Department(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=10)
    ManagerID = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='ManagerID'
        )

    ManagerName = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='ManagerName'
        )

    ACTIVE_CHOICES = [
        (True, 'Active'),
        (False, 'Inactive'),
    ]

    DepartmentActiveStatus = models.BooleanField(
        default=True,  # Set the default status to Active
        choices=ACTIVE_CHOICES,
    )
    DepartmentCreatedDate = models.DateField(null=True)
    DepartmentUpdatedDate = models.DateField(null=True)

    def __str__(self):
        return self.DepartmentName
    


# Documents Model/Table
class Documents(models.Model):
    DocumentID = models.AutoField(primary_key=True)
    ExpenseID = models.ForeignKey(Expense, on_delete=models.CASCADE, null=False)
    SupportingDocuments = models.FileField(upload_to='Images/')  # Use FileField for documents

    
    def __str__(self):
        # return self.SupportingDocuments
        return self.SupportingDocuments.name  # Return the file name using the .name object


# Dispute Model/Table
class Dispute(models.Model):
    DisputeID = models.AutoField(primary_key=True)

    ExpenseID = models.ForeignKey(
        Expense, 
        on_delete=models.CASCADE, 
        null=False, 
        related_name='disputed_expense'
        )
    
    EmployeeID = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE, 
        null=False, 
        related_name='dispute_raised_by'
        )
    
    ReasonForDisputes = models.TextField(max_length=250, null=False)

    def __str__(self):
        return f"Dispute #{self.DisputeID} (Expense: {self.ExpenseID}, Raised by: {self.EmployeeID})"
