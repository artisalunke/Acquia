.. include:: /common/global.rst

|acquia-product:ac| glossary
============================

This page defines some of the important terms used in the |acquia-product:ui|. We've made some changes in terminology from the previous version of the |acquia-product:ui|, and this page also points out those changes.

.. list-table::
 :widths: 20 80
 :header-rows: 1

 * - Term
   - Definition
 * - `Administrator </acquia-cloud/teams/organizations#roles>`__
   - *Acquia Cloud special role that has all of the possible permissions for all of the applications in an organization.* |br| 
     You cannot customize the *Administrator* role to have less than all the permissions. They do not need to be assigned to a team in order to act on an application. An organization can have more than one *Administrator*. The *Owner* of an organization also acts in all respects as an *Administrator*.
 * - `Application </acquia-cloud/manage#app>`__
   - *A software product that implements a web service, such as a Drupal-based web site or a web-accessible API.* |br| 
     In a modern digital portfolio, applications may encompass mobile or wearable apps, IoT, and future interface devices. In |acquia-product:ac|, an application specifically refers to the software product as an entity in itself, separate from the potentially many installations of the application in different environments, such as Production, or Development, that may use specific domain names, with specific content. Applications have a lifecycle and typically have multiple versions. An application is primarily made up of its program code, such as Drupal core plus contributed and custom modules, along with static assets such as images and stylesheets for its visual theme. |br| 
     In the legacy Acquia Cloud interface, applications were referred to as *sites* or *websites*, and sometimes as *site groups*.
 * - `Environment </acquia-cloud/manage/environments>`__
   - *Separate areas in your application that you can use to maintain a clear and orderly workflow as you develop, test, and publish your applications.* |br| 
     An application is deployed on each of its environments, but each environment may be in a different state, with its own database and possibly a different code branch or tag deployed. Each environment has a URL at which its application can be viewed, but only the Production environment's URL is designed to be visible to the application's users (website visitors). The `number of environments available to you </acquia-cloud/manage/environments>`__ depends on your Acquia subscription.
 * - `Organization </acquia-cloud/teams/organizations>`__
   - *A group of subscriptions, applications, and teams in Acquia Cloud.* |br| 
     An organization can represent different business objects for different entities. For example, all of a company's applications might be grouped under a single organization, or under independent organizations for separate business units. Your organizations are set up by Acquia when you create an Acquia subscription. Each subscription, including its applications, and each team belongs to one and only one organization. A team member may be on teams that are assigned to any number of organizations. |br| 
     In the legacy |acquia-product:ac| interface, organizations were referred to as *subscription groups*.
 * - `Owner </acquia-cloud/teams/organizations#roles>`__
   - *Acquia Cloud special role that has all of the possible permissions for all of the applications in an organization.* |br| 
     You cannot customize the *Owner* role to have less than all the permissions. They do not need to be assigned to a team in order to act on an application. An organization must always have exactly one *Owner*. The *Owner* of an organization also acts in all respects as an *Administrator*.
 * - Profile
   - *Editable information about a user in the Acquia Cloud interface, including password, name, contact information, API credentials, and two-step verification settings.* |br| 
     Everyone who is registered as a user for the Acquia Cloud interface has a personal profile that they can access by clicking their photo or avatar in the upper right corner of the Acquia Cloud interface.
 * - Scheduled job
   - *Automated maintenance task or job set to run at scheduled intervals using the Scheduled Jobs page in the Acquia Cloud interface.* |br| 
     In the legacy Acquia Cloud interface, this task was handled on the Cron page. For more information, see `Using scheduled jobs to maintain your application </acquia-cloud/manage/cron>`__.
 * - Subscription
   - *A set of entitlements that you have purchased from Acquia, including how many applications you can host on Acquia Cloud, what hardware they run on, and what level of support you are entitled to.* |br| 
     Each organization can have one or more subscriptions, which are available at three basic levels: |acquia-product:ace|, |acquia-product:acs|, and |acquia-product:acfs|.
 * - Team
   - *Organizational unit of users who work on developing and managing Acquia Cloud applications, and are assigned to applications.* |br| 
     A user's permissions for an application are defined by the role assigned to the user as a team member on that team. For example, some roles allow a user to act only on non-Production environments for the team's applications. For more information, see `Managing users, teams, roles, and permissions </acquia-cloud/teams>`__.
