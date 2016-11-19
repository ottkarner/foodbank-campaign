from django.contrib import admin
from django.db.models import F, Sum, IntegerField
from django.utils.translation import ugettext_lazy as _

import nested_admin

from locations.models import District, Location
from campaigns.models import CampaignLocationShift
from campaigns.admin import VolunteerParticipantInline


class CampaignShiftInline(nested_admin.NestedTabularInline):
    model = CampaignLocationShift
    exclude = ['volunteers']
    inlines = [VolunteerParticipantInline]
    extra = 0


class LocationAdmin(nested_admin.NestedModelAdmin):
    search_fields = ['name', 'address',
            'campaignlocationshift__volunteers__first_name',
            'campaignlocationshift__volunteers__last_name']
    list_filter = ['district']
    inlines = [CampaignShiftInline]
    list_display = ['name', 'volunteers_count', 'free_places']

    def volunteers_count(self, obj):
        return obj.campaignlocationshift_set.aggregate(
                count=Sum('volunteers__participant_count'))['count']
    volunteers_count.short_description = _('Volunteers count')

    def free_places(self, obj):
        total_places = obj.campaignlocationshift_set.aggregate(total=Sum(
            'total_places'))['total']
        taken_places = obj.campaignlocationshift_set.aggregate(taken=Sum(
            'volunteers__participant_count'))['taken']
        return int(total_places or 0) - int(taken_places or 0)
    free_places.short_description = _('Free places')


admin.site.register(District)
admin.site.register(Location, LocationAdmin)
