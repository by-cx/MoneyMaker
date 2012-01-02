import datetime
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from money.models import Bill
from django.utils.translation import ugettext_lazy as _

class BillCreateView(CreateView):
    def form_valid(self, form):
        ret = super(BillCreateView, self).form_valid(form)
        self.object.user = self.request.user
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, _("Item has been created"))
        return ret

class StatsView(TemplateView):
    template_name = "stats.html"

    def year_stats(self):
        year = self.kwargs.get("year") if self.kwargs.get("year") else datetime.date.today().year
        #months, total
        stats = [
                {"count": 0, "name": _("January"), "categories": {}, "fixed": 0, "regularly": 0},
                {"count": 0, "name": _("February"), "categories": {}, "fixed": 0, "regularly": 0},
                {"count": 0, "name": _("March"), "categories": {}, "fixed": 0, "regularly": 0},
                {"count": 0, "name": _("April"), "categories": {}, "fixed": 0, "regularly": 0},
                {"count": 0, "name": _("May"), "categories": {}, "fixed": 0, "regularly": 0},
                {"count": 0, "name": _("June"), "categories": {}, "fixed": 0, "regularly": 0},
                {"count": 0, "name": _("July"), "categories": {}, "fixed": 0, "regularly": 0},
                {"count": 0, "name": _("August"), "categories": {}, "fixed": 0, "regularly": 0},
                {"count": 0, "name": _("September"), "categories": {}, "fixed": 0, "regularly": 0},
                {"count": 0, "name": _("October"), "categories": {}, "fixed": 0, "regularly": 0},
                {"count": 0, "name": _("November"), "categories": {}, "fixed": 0, "regularly": 0},
                {"count": 0, "name": _("December"), "categories": {}, "fixed": 0, "regularly": 0}
        ]
        total = {"fixed": 0, "regularly": 0, "count": 0}
        for bill in Bill.objects.filter(date__year=year).all():
            if bill.category.name not in stats[bill.date.month-1]["categories"]:
                stats[bill.date.month-1]["categories"][bill.category.name] = 0
            stats[bill.date.month-1]["categories"][bill.category.name] += bill.value
            stats[bill.date.month-1]["count"] += 1
            total["count"] += 1
            if bill.category.fixed:
                total["fixed"] += bill.value
                stats[bill.date.month-1]["fixed"] += bill.value
            else:
                total["regularly"] += bill.value
                stats[bill.date.month-1]["regularly"] += bill.value
        total["total"] = total["fixed"] + total["regularly"]
        return stats, total, year

    def get_context_data(self, **kwargs):
        context = super(StatsView, self).get_context_data(**kwargs)
        data = self.year_stats()
        context["year_stats"] = data[0]
        context["year_stats_total"] = data[1]
        context["year_stats_year"] = data[2]
        return context
