from users.models import User

def generate_user_report():
    total = User.objects.count()
    active_users = User.objects.filter(is_active=True).count()
    return {
        'total_users': total,
        'active_users': active_users,
    }
