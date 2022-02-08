from django.contrib import admin
from .models import *

class Announced_pu_results(admin.ModelAdmin):
    list_display = ['polling_unit_unique_id',
                    'party_abbreviation',
                    'party_score',
                    ]
    
    list_filter = ['polling_unit_unique_id',
                    'party_abbreviation',
                    'party_score',
                    ]

    search_fields = [
                    'polling_unit_unique_id',
                    'party_abbreviation'
                    ]


class Polling_Unit(admin.ModelAdmin):
    list_display = ['polling_unit_id',
                    'lga_id',
                    'polling_unit_name',
                    'polling_unit_number'
                    ]
    
    list_filter = ['polling_unit_id',
                    'lga_id',
                    'polling_unit_name',
                    'polling_unit_number'
                    ]

    search_fields = [
                    'lga_id',
                    ]


admin.site.register(lga)
admin.site.register(agentname)
admin.site.register(announced_lga_results)
admin.site.register(announced_pu_results,Announced_pu_results)
admin.site.register(announced_state_results)
admin.site.register(announced_ward_results)
admin.site.register(party)
admin.site.register(polling_unit,Polling_Unit)
admin.site.register(states)
admin.site.register(ward)