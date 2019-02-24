.. include:: /common/global.rst

Designing your content architecture
======================================================

.. container:: internal-navigation

   **Platform governance**

   * :doc:`Intro </resource/governance>`
   * :doc:`Types </resource/governance/types>`
   * :doc:`Models </resource/governance/models>`
   * Architect
   * :doc:`Build </resource/governance/build>`
   * :doc:`Migrate </resource/governance/migrate>`
   * :doc:`Maintain </resource/governance/maintain>`

When designing a platform, you will want to document both your content
model and your content architecture as part of your governance plan.
Your content model will define the types of content that you plan on
hosting, and their fields and organization. Your content architecture
documents how to organize that content in a manner that is meaningful
and intuitive for the users of your platform.

Content architecture is important for several different user groups,
including the following:

-  *Content​ ​administrators​* create content for the platform, and need
   content models that are intuitive and consistent.
-  *Designers*\ ​ ​need access to a fully-defined content model,
   including content available and unavailable to end users, to create
   and update their designs to accommodate the current state of the
   content model.
-  *Developers* need an complete and accurate content model to configure
   the content management system. A lack of current knowledge about the
   content model can lead to technical debt and increased
   time-to-market.

Defining content architecture
-----------------------------

Drupal’s ease of use means that content architects can add multiple
fields to content types with a few clicks of a mouse, making it simple
to create an overly-complicated content model. A well-defined content
architecture encourages developers to build a structure that best and
most efficiently supports the company’s business goals and
functionality.

When defining your content architecture, we recommend the following
steps:

-  `Create a content inventory <#inventory>`__
-  `Create an editorial calendar <#calendar>`__
-  `Determine placement and presentation <#placement>`__

Creating a content inventory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your first step in developing your content architecture involves
performing a content inventory: a list of all content on your platform
that will help you determine what content you need to include, but how
it should be categorized and presented. This process will also help you
determine content you need that does not yet exist, and assist you in
creating the tasks in your project plan relating to content production
and editing.

When conducting a content inventory, be sure to complete the following
steps:

-  Assess every piece of content to determine its purpose
-  Document critical content details, including:

   -  Content status
   -  Navigation level
   -  Title
   -  URL
   -  File format
   -  Author
   -  Taxonomy and tagging

-  Determine how your content should be handled during your
   re-platforming efforts, based on the following questions:

   -  Should it be removed?
   -  Should it be rewritten or edited?
   -  Should it be moved from its current location?
   -  Should it be split into new pieces, or combined with others?
   -  Is it missing, and should it be created?

Creating an editorial calendar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After creating a content inventory, you should create an editorial
calendar to define the frequency of content creation, review,
separation, or removal. Your calendar should also indicate who owns each
piece of content or content section.

Your editorial calendar may be heavily informed by your marketing
campaigns, seasons of the year, known organizational events, or
compliance reviews. You should also factor in the lead time needed for
developing and refining content from initial assignment to publication.

Determining placement and presentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you create your content list, the next step is to determine how
the content fits together in your platform. Although some content may
appear to be different, or even appear in different places on your
platform, they may be a single content type if their attributes are
similar enough.

You should also consider how your content fits together:

-  Does your content need an organized data model containing specific
   structural elements for sorting and filtering?
-  Will your content be used in a single place in a single website, or
   does it need to be reusable across multiple places in a single
   website, or through multiple websites using [hub]? If yes, you should
   determine how content is cross-referenced.
-  What fields, taxonomies, and metadata are needed in your content?

Decisions related to content architecture and content modeling should be
made both early and often. As these decisions affect the technical
architecture of your platform, any significant changes could cause
delays in your project, and could make your content architecture and
content model a moving target instead of a defined process with a clear
plan.

On the next page in this series, you'll learn more about `building
governance policies </resource/governance/build>`__ to deal with
feature requests and approvals.
