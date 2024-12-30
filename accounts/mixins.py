
from django.shortcuts import redirect

# মিক্সিন হলো একটি ক্লাস যা অন্য ক্লাসের মধ্যে রি-ইউজেবল ফাংশনালিটি যোগ করতে ব্যবহৃত হয়
# এটি মাল্টিপল ইনহেরিটেন্স এর মাধ্যমে কাজ করে এবং কোড পুনঃব্যবহার করতে সাহায্য করে
# মিক্সিন ক্লাস নিজে কখনও ইনস্ট্যান্স তৈরি করে না, এটি শুধুমাত্র অন্য ক্লাসের সাথে মিশ্রিত হয়
class LogoutRequiredMixin(object):
    """Verify that the current user is not logged in."""
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)