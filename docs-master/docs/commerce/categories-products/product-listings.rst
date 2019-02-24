.. include:: /common/global.rst

Product listings best practices
===============================

The |acquia-product:acm| modules create two entities when synchronizing
products to Drupal: a product entity and a SKU entity. When creating
product listings, you should use the product entity and reference fields
and values from the SKU entity where possible.

Search API indexes can be created for the product entity type to
facilitate creating product listings, related product lists, and search
listings. Facets can be created with the indexed values, and all content
from the commerce backend can be indexed.

The product and SKU entities have a loose reference in the form of a
custom *SKU Reference* field. The SKU Reference field is not a typical
entity reference field; it does not require the entity to exist and is a
free text text field. The reference is handled by the field type plugin,
and it creates a computed property that attempts to load a referenced
entity when the field is being used.

Because a SKU is not easily relatable to a product in a view, you should
instead use a search index-based view.

Keyword search listings and facet filtering
-------------------------------------------

Search API-based views can be used for products. Before you create a
view, determine if Solr should be used to create your product listings
based on the following questions:

-  How many products are going to be included in the index?
-  How many fields do you need to index?

If using a Search API-based view makes sense for your website, you can
use the information in the following sections to guide you.

Available fields
~~~~~~~~~~~~~~~~

Many SKU attributes will not be available in views without custom
handling. For information about special handling for attributes, see
`SKU attributes, product options, and product
categories </commerce/categories-products/sku-attributes>`__.

Additionally, keyword search and facet fields must be added to the
search index to be available as search and facet fields.

Configure a Product search index
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using Search API, a developer can create product search indexes in any
available search backend. To do this, create a `Search
server </acquia-search/activate>`__, and then create a new `search
index </acquia-search/indexing>`__ based on the following item
selections:

-  Datasource – **Content**
-  Select **None except those selected**
-  Type – **product content**
-  Configure the fields (``field_skus`` can be expanded to include
   entity values)

Facets
~~~~~~

By using Search API, a developer can enable the Facets module, which
allows for the creation of facets from the values available in the
index.

After you enable the `Facet </acquia-search/facets/configure>`__ module,
configure your facets based on the search display. Facets require the
field to be included in the index.

Related products
----------------

The following methods are available to display products that are related
to the product being displayed:

-  *Dynamic lists*
   The product nodes have a category field, which can be used to create
   dynamic product relationships. These relationships can be used to
   create a related product list.
-  *Curated lists*
   Magento allows one to manage lists of related SKUs to a SKU. These
   fields, while not added initially to the SKU entity, can be added by
   a custom module. These fields will typically be a multi-value text
   field that will accept lists of SKUs from Magento. This makes it
   possible to easily render related products wherever products are
   displayed.
