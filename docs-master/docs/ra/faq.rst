.. include:: /common/global.rst

Remote Administration FAQ
=========================

This is a list of frequently asked questions about Acquia Remote
Administration and Automation processes.

What if I did not get a ticket?

Only websites that are compatible with automation will get a ticket
within the 24-48 hour window. If your subscription did not get a ticket,
ensure that your `RA Preferences </ra/preferences>`__ are set to
**Inform Only** or **Full Deploy**. If your preferences are set
correctly, `contact Acquia Support </support#contact>`__. It is possible
that the subscription is not compatible with automation, or automation
was unable to complete the update due to an error. We will likely have
an internal log of this error, and can assist with troubleshooting.
Premium RA clients are eligible for manual updates.

What if my subscription is not compatible with automation?

.. raw:: html

   <div class="answ">

The answer to this question is based on your subscription level:

-  **RA Standard** - Compatibility with automation is the responsibility
   of your development team.
-  **RA Premium** - Acquia Support Engineers can assist you in
   troubleshooting and modifying your codebase to ensure that it is
   compatible with automation.

.. raw:: html

   </div>

Can I schedule when my updated code is pushed to production?

Yes. For more information, see `Scheduling Production Deploy
Windows </ra/security#scheduling>`__.

How many security updates per year does the Remote Administration team
estimate will affect any given website?

.. raw:: html

   <div class="answ">

There are two types of security updates that Drupal websites need to be
aware of: updates for Drupal core and updates for Drupal modules.

To give you an idea of the number of core updates per year, in 2014 the
`Drupal Security Team <https://www.drupal.org/security-team>`__
announced core `security releases <https://www.drupal.org/security>`__
in November, October, August, July, April, and January.

Drupal modules are subject to security updates at any point in time, as
they are maintained by individuals or small groups. All modules are
constructed differently, by different people. As a result, we cannot
extrapolate how often updates might be necessary for your website. Also,
most Drupal 7 modules, at this point in Drupal 7's lifecycle, do not
often need security updates.

.. raw:: html

   </div>

How often does the Remote Administration team check for security updates
to core and contributed modules?

.. raw:: html

   <div class="answ">

The Remote Administration team monitors for security releases based on
the Drupal Security team’s
`schedule <https://www.drupal.org/node/1173280>`__. Security release
windows for Drupal are based on the following timeline:

-  *Drupal contributed projects* - Every Wednesday
-  *Drupal core* - One Wednesday a month (usually the third Wednesday)

A release window does not necessarily indicate that a release will occur
on that date, but it exists so that site administrators can know in
advance which days they should be aware of a possible security release.
In the unusual case of a highly critical security issue, such as one
which is being actively exploited in the wild, releases can occur
outside of the normal release window.

If we are aware of particularly hazardous security updates available for
common modules, or during long gaps between Drupal core security
releases, we will periodically proactively contact Remote Administration
customers to inform them that some module security updates are pending
that we can perform.

.. raw:: html

   </div>

What is the delay between Acquia detecting a security update and Acquia
creating the branch and deploying on RA environment?

Acquia usually begins initiating updates within one day of a security
release's availability. Depending on the complexity of the release and
number of customers who want it, our semi-automated systems are usually
able to update all Remote Administration customers within 48 hours of
the release.

Is it typical for customers to bundle security updates, regression
testing, and deployment to production in batches (once per month or
quarter)? In this case how do customers identify critical security
updates that they must check and authorize without delay?

.. raw:: html

   <div class="answ">

For customers who cannot deploy new code to Production on-demand for
various reasons, a quarterly release timeline generally works well. This
gives them time to shift resources and schedule their testing and
deployment accordingly. Some customers require immediate deployment of
all security changes, in which case the update may need to be
self-applied and deployed.

Generally, we can neither prioritize certain customers over others or
predict when our semi-automated scripts will hit certain subscriptions
in our list. Because of this, depending on the complexity of the update
and number of customers responding to pending updates, one update could
see your subscription having an update applied and deployed to your RA
environment within a few days, while another update could take one to
two weeks.

We recommend that customers test core updates first, and then apply and
test module security updates one at a time. This ensures core security,
and saves effort if issues arise and that require changes to be reverted
module-by-module.

In the case of particularly hazardous Drupal core updates, we will note
in our communications that they must be deployed as soon as possible,
and explain why. If we are aware of a particularly hazardous module
security update, we will also notify customers. This happens less
frequently, and the burden of monitoring falls on the customers who are
using specific modules.

There are separate security updates applicable to our platform which may
require testing throughout the year. See the `Acquia security update
list <%5Bacquia-product:kb%5Darticles/acquia-security-update-list>`__
and the `Software end-of-life schedule </support/eol>`__ for details on
these updates.

.. raw:: html

   </div>

May I use the RA environment as a mirror for my Production environment?

.. raw:: html

   <div class="answ">

The `RA environment </ra/environment>`__ is provided as a mechanism for
Acquia's Remote Administration team to deploy security-related updates
in a semi-automated fashion for testing by customers. This is done using
Acquia automation, and we do not expect any `customer code or database
deployments to use that environment </ra/environment#testing>`__.

The majority of RA environments are on shared hardware, which other
customers are using for testing their updates. To not overload the
shared hardware, at any given point in time we are working only with a
limited number of customers on these servers.

.. raw:: html

   </div>

When will I receive my updates?

The RA automation queue is generally run once a week, timed to accompany
SA announcements (typically on
`Wednesdays <%20https://www.drupal.org/node/1173280>`__). You should
receive an update within 48 hours of initiation of an automated run. For
details about when updates occur, see `Ticket
timelines </ra/security#timelines>`__.

How long does the update process take?

The `security update process </ra/security-update-process>`__ works at
the speed of your team, and depends on your team following the
`recommended workflow </ra/workflow>`__.

Will declining to use an update branch affect future updates for us?

Declining to take action on any specific update branch issued by the RA
team will not affect future updates. Any security updates not acted upon
and promoted to Production before the next run of Acquia automation will
result in an update branch that incorporates all available security
updates.
