from django.views.generic.edit import CreateView

class BillCreateView(CreateView):
    def form_valid(self, form):
        ret = super(BillCreateView, self).form_valid(form)
        self.object.user = self.request.user
        self.object.save()
        return ret
