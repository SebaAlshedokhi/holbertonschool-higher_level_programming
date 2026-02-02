def generate_invitations(template, attendees):
    try:         #تتأكد من نوع البيانات المدخلة
        isinstance(template, 'string')
        isinstance(attendees, 'dict')
    except ValueError:        #إذا غير كذا → اطبع رسالة خطأ وأوقف التنفيذ.
        exit
    
