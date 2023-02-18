jQuery(document).ready(function() {

  // Get the dropdown field and parent elements
  var dropdownField = jQuery('#id_invoice_type');
  var parentElements = {
    total_work_done: jQuery('#id_total_work_done').closest('.form-row'),
    previous_work_done: jQuery('#id_previous_work_done').closest('.form-row'),
    balance_work_done: jQuery('#id_balance_work_done').closest('.form-row'),
    current_work_done: jQuery('#id_current_work_done').closest('.form-row'),
  };

  // Hide parent elements by default
  Object.values(parentElements).forEach(element => element.hide());

   // Show or hide parent elements based on the value of dropdownField
  dropdownField.change(function() {
    const shouldShow = dropdownField.val() !== 'advance';
    Object.entries(parentElements).forEach(([key, element]) => {
        element.toggle(shouldShow);
    });
  });
  dropdownField.change();
});