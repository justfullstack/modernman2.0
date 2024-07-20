from django.forms import inlineformset_factory
from checkout import models


# CartlineSet formset will automatically build forms for all basket lines
# connected to the basket specified; the only editable fields will
# be quantity and there will be no extra form to add new entries, 
# as we do that through the add_to_basket view.

CartLineFormSet = inlineformset_factory(
            models.Cart,
            models.CartLine,
            fields=('quantity', ),
            extra=0,
        )

