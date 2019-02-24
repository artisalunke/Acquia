.. include:: /common/global.rst

updatePerson - |acquia-product:cha| JavaScript API
==================================================

|acquia-product:cha| uses the ``updatePerson`` API function to update
user-defined |person attributes|_ without
creating an `Event </lift/omni/event>`__ record or updating the
`Touch </lift/omni/touch>`__ record. This can be helpful when there is
data from another source that you want to append to the person profile,
such as firmographic or demographic data. You can provide descriptive
names for these attributes in |acquia-product:alw|, which are then
displayed in the `visitor profile summary </lift/profile-mgr/person/profile>`__ 
and the `segment builder </lift/profile-mgr/segment>`__, using the 
`Content metadata page </lift/profile-mgr/segment/category#editing>`__.

.. |person attributes| replace:: ``Person`` attributes
.. _person attributes: /lift/omni/person

Capturing person attributes
---------------------------

Add the following code to your webpage:

.. code-block:: none

   <script type="text/javascript">
   _tcaq.push( ['updatePerson',
   {'person_udf5':'attributedata1', 'person_udf6':'attributedata2', 'person_udf7': 'attributedata3' }
   ] );
   </script>

where ``person_udf`` is a user-defined field for a person and
``attributedata`` is the information to add to the person. Up to 50
fields for values can be defined.

|acquia-product:cha| captures the fields and associates them with the
website visitor's information.

Example usage
~~~~~~~~~~~~~

The following example sets user-defined fields ``5``, ``6``, and ``7``
to firmographic values associated with the business that the person
works for - the company ``SMB``, categorized as ``Retail``, with
``0-50 employees``:

.. code-block:: none

   <script type="text/javascript">
   _tcaq.push( ['updatePerson',
   {'person_udf5':'SMB', 'person_udf6':'Retail', 'person_udf7': '0-50 employees' }
   ] );
   </script>
