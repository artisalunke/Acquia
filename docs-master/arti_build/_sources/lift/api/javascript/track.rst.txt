.. include:: /common/global.rst

setDoNotTrack - |acquia-product:cha| JavaScript API
===================================================

Targeting and recommending content to website visitors requires that you
collect data about those visitors. If you don't know information about
visitors, you cannot effectively display personalized content that
intrinsically meets their needs.

Some visitors, however, do not want to be tracked. To accommodate this
situation, you can use the |liftapi|_ to add functionality to your website that
allows visitors the ability to opt in or out of being tracked.


.. |liftapi| replace:: \ |acquia-product:cha|\  Javascript API
.. _liftapi: /lift/javascript

Using cookies to track visitors
-------------------------------

To identify website visitors between their visits, |acquia-product:cha|
uses *cookies*, or small text files stored in each visitor's local
browser cache. Each time your website is displayed by a visitor,
|acquia-product:cha| searches for any of its identifier cookies in an
attempt to match the visitor with information stored in
|acquia-product:cha|. Information about the visit can then be associated
with the appropriate visitor for a continued refinement of the visitor's
profile.

If a user indicates to |acquia-product:cha| that they do not want to be
tracked, |acquia-product:cha| updates one or both of the following
cookies in the visitor's local browser cache:

-  ``tc_dnt`` - This cookie is populated if do not track is enabled.
-  ``tc_3dnt`` - This cookie is populated if do not track is enabled and
   third-party cookies are enabled. For more information about using
   third-party cookies, see `Managing your visitor capture
   settings </lift/profile-mgr/admin/javascript>`__.

When do not track is enabled for a visitor, the visitors' person record
in the |acquia-product:cha| service is updated with a flag to not track
his or her activities. From that point on, no additional information
about the visitor is sent to the |acquia-product:cha| service.

For more information about the cookies that |acquia-product:cha| uses to
track website visitors, see `Cookies used by Acquia Lift </lift/service/cookies>`__.

Allowing visitors to control their tracking settings
----------------------------------------------------

Using the `JavaScript API </lift/javascript>`__, |acquia-product:cha|
allows you to update your website with settings that visitors can use to
control their own do not track settings.

Depending on a visitor's requirement, use the appropriate JavaScript
function call from the following list with whatever decision-making
element you add to your website:

-  *Enable the do not track feature for a visitor*

   ``_tcaq.push(['setDoNotTrack', true]);``

-  *Disable the do not track feature for a visitor* — this does not
   currently work; the cookies must be deleted manually.

   ``_tcaq.push(['setDoNotTrack', false]);``


Monitoring visitors' do not track settings
------------------------------------------

In the |acquia-product:lpm| interface, you can review properties about
visitors in the Person details page. To determine if a visitor has
enabled or disabled the do not track setting on your website, review the
visitor's **Do Not Track** property:

-  **No** - Do not track is disabled
-  **Yes** - Do not track is enabled

For more information about reviewing visitors' Person details, see
`Examining visitor information </lift/profile-mgr/person>`__.
