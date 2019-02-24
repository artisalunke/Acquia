.. include:: /common/global.rst

Define a custom config entity
===================================

.. container:: message-status

   Fast Track to Drupal 8 Coding – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/fast-track-drupal-8-coding

.. |Previous lesson| replace:: Block users based on a certain criteria
.. _Previous lesson: /tutorials/fast-track-drupal-8-coding/block-users-based-certain-criteria

.. |Next lesson| replace:: Store data in a custom table
.. _Next lesson: /tutorials/fast-track-drupal-8-coding/store-data-custom-table


Lesson Goal
-----------

.. container:: message-status

   Create a custom config entity to store different emails configured per
   content type to send updates.

Implementation Method
---------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Drupal Version 
     - Method
   * - Drupal 7
     - *The concept of config entity is new in Drupal 8 and was not possible in Drupal 7* 
   * - Drupal 8
     - `Custom configuration entity <https://www.drupal.org/docs/8/api/configuration-api/creating-a-configuration-entity-type-in-drupal-8>`__


Drupal 8 method
---------------

#. Create a new module by adding the following code in the ``lotus.info.yml`` file:

   .. code-block:: yaml

      name: 'Lotus'
      description: 'Provides a configuration entity to store email per node type'
      type: module
      core: 8.x

#. Create routes for the new entity by adding the following code in the ``lotus.routing.yml`` file:

   .. code-block:: yaml
      :linenos:

      entity.lotus.collection:
        path: '/admin/config/system/lotus'
        defaults:
          _entity_list: 'lotus'
          _title: 'Lotus configuration'
        requirements:
          _permission: 'administer site configuration'
      entity.lotus.add_form:
        path: '/admin/config/system/lotus/add'
        defaults:
          _entity_form: 'lotus.add'
          _title: 'Add Lotus configuration'
        requirements:
          _permission: 'administer site configuration'

      entity.lotus.edit_form:
        path: '/admin/config/system/lotus/{lotus}'
        defaults:
          _entity_form: 'lotus.edit'
          _title: 'Edit Lotus configuration'
        requirements:
          _permission: 'administer site configuration'

      entity.lotus.delete_form:
        path: '/admin/config/system/lotus/{lotus}/delete'
        defaults:
          _entity_form: 'lotus.delete'
          _title: 'Delete Lotus configuration'
        requirements:
          _permission: 'administer site configuration'

#. Add links to the main navigation. To do this, complete the following steps:

   a. Add the following code in the ``lotus.links.menu.yml`` file:

      .. code-block:: yaml

          entity.lotus_collection:
          title: 'Lotus configuration'
          parent: system.admin_config_system
          route_name: entity.lotus.collection
          weight: 99

   #. Add the following code in the ``lotus.links.action.yml`` file:

      .. code-block:: yaml

         entity.lotus_add_form:
          route_name: 'entity.lotus.add_form'
          title: 'Add Lotus Configuration'
          appears_on:
            - entity.lotus.collection

#. Create a schema by adding the following code in the ``lotus/config/schema/lotus.schema.yml`` file:

   .. code-block:: yaml

      lotus.lotus.*:
        type: config_entity
        label: 'lotus config'
        mapping:
          id:
            type: string
            label: 'ID'
          label:
            type: label
            label: 'Label'
          content_type:
            type: string
            label: 'Content Type'
          email:
            type: email
            label: 'Email'

#. Define the custom entity by completing the following steps:

   a. Add the following code in the ``lotus/src/LotusInterface.php`` file:
  
      .. code-block:: php

          <?php
          namespace Drupal\lotus;

          use Drupal\Core\Config\Entity\ConfigEntityInterface;

          /**
          * Provides an interface defining an Example entity.
          */
          interface LotusInterface extends ConfigEntityInterface {
            // Add get/set methods for your configuration properties here.
          }

   #. Add the following code in the ``lotus/src/Entity/Lotus.php`` file:
      
      .. code-block:: php

         <?php
         namespace Drupal\lotus\Entity;

         use Drupal\Core\Config\Entity\ConfigEntityBase;
         use Drupal\lotus\LotusInterface;

         /**
         * Defines the lotus entity.
         *
         * @ConfigEntityType(
         *   id = "lotus",
         *   label = @Translation("Lotus"),
         *   handlers = {
         *     "list_builder" = "Drupal\lotus\Controller\LotusListBuilder",
         *     "form" = {
         *       "add" = "Drupal\lotus\Form\LotusForm",
         *       "edit" = "Drupal\lotus\Form\LotusForm",
         *       "delete" = "Drupal\lotus\Form\LotusDeleteForm",
         *     }
         *   },
         *   config_prefix = "lotus",
         *   admin_permission = "administer site configuration",
         *   entity_keys = {
         *     "id" = "id",
         *     "label" = "label",
         *   },
         *   links = {
         *     "edit-form" = "/admin/config/system/lotus/{lotus}",
         *     "delete-form" = "/admin/config/system/lotus/{lotus}/delete",
         *   }
         * )
         */
         class Lotus extends ConfigEntityBase implements LotusInterface {

         /**
         * The lotus ID.
         *
         * @var string
         */
         public $id;

         /**
         * The lotus label.
         *
         * @var string
         */
         public $label;

         // Your specific configuration property get/set methods go here,
         // implementing the interface.
        }

#. Create forms and controllers for the required functionality by
   completing the following steps:

   a. Add the following code in the
      ``lotus/src/Controller/LotusListBuilder.php`` file:

      .. code-block:: php
         :linenos:

          <?php
          namespace Drupal\lotus\Controller;

          use Drupal\Core\Config\Entity\ConfigEntityListBuilder;
          use Drupal\Core\Entity\EntityInterface;

          /**
          * Provides a listing of lotus.
          */
          class LotusListBuilder extends ConfigEntityListBuilder {

            /**
            * {@inheritdoc}
            */
            public function buildHeader() {
              $header['label'] = $this->t('lotus');
              $header['id'] = $this->t('Machine name');
              return $header + parent::buildHeader();
            }

            /**
            * {@inheritdoc}
            */
            public function buildRow(EntityInterface $entity) {
              $row['label'] = $this->getLabel($entity);
              $row['id'] = $entity->id();

              // You probably want a few more properties here...
              return $row + parent::buildRow($entity);
            }

          }

   #. Add the following code in the ``lotus/src/Form/LotusForm.php``
      file:

      .. code-block:: php
         :linenos:

          <?php
          namespace Drupal\lotus\Form;

          use Drupal\Core\Entity\EntityForm;
          use Drupal\Core\Entity\Query\QueryFactory;
          use Drupal\Core\Form\FormStateInterface;
          use Drupal\Core\Entity\EntityManagerInterface;
          use Symfony\Component\DependencyInjection\ContainerInterface;

          /**
          * Form handler for the lotus add and edit forms.
          */
          class LotusForm extends EntityForm {

            protected $entityQuery;

            protected $entityManager;

            /**
            * Constructs an lotusForm object.
            *
            * @param \Drupal\Core\Entity\Query\QueryFactory $entity_query
            *   The entity query.
            * @param \Drupal\Core\Entity\EntityManagerInterface $entity_manager
            *   The entity Manager.
            */
            public function __construct(QueryFactory $entity_query, EntityManagerInterface $entity_manager) {
              $this->entityQuery = $entity_query;
              $this->entityManager = $entity_manager;
            }

            /**
            * {@inheritdoc}
            */
            public static function create(ContainerInterface $container) {
              return new static(
                $container->get('entity.query'),
                $container->get('entity.manager')
              );
            }

            /**
            * {@inheritdoc}
            */
            public function form(array $form, FormStateInterface $form_state) {
              $form = parent::form($form, $form_state);

              $lotus = $this->entity;

              $form['label'] = array(
                '#type' => 'textfield',
                '#title' => $this->t('Label'),
                '#maxlength' => 255,
                '#default_value' => $lotus->label(),
                '#description' => $this->t("Label for the lotus."),
                '#required' => TRUE,
              );
              $form['id'] = array(
                '#type' => 'machine_name',
                '#default_value' => $lotus->id(),
                '#machine_name' => array(
                  'exists' => array($this, 'exist'),
                ),
                '#disabled' => !$lotus->isNew(),
              );

              $content_types = $this->entityManager->getStorage('node_type')->loadMultiple();
              $content_types_list = [];
              foreach ($content_types as $content_type) {
                $content_types_list[$content_type->id()] = $content_type->label();
              }

              $form['content_type'] = array(
                '#type' => 'select',
                '#default_value' => $lotus->get('content_type'),
                '#description' => $this->t('Select content type to add Email Address'),
                '#required' => TRUE,
                '#options' => $content_types_list,
              );

              $form['email'] = array(
                '#type' => 'email',
                '#title' => $this->t('Email'),
                '#maxlength' => 255,
                '#default_value' => $lotus->get('email'),
                '#description' => $this->t("Enter email address to send notifications"),
                '#required' => TRUE,
              );

              // You will need additional form elements for your custom properties.
              return $form;
            }

            /**
            * {@inheritdoc}
            */
            public function save(array $form, FormStateInterface $form_state) {
              $lotus = $this->entity;
              $status = $lotus->save();

              if ($status) {
                drupal_set_message($this->t('Saved the %label lotus.', array(
                  '%label' => $lotus->label(),
                )));
              }
              else {
                drupal_set_message($this->t('The %label lotus was not saved.', array(
                  '%label' => $lotus->label(),
                )));
              }

              $form_state->setRedirect('entity.lotus.collection');
            }

            /**
            * Helper function to check whether an lotus configuration entity exists.
            */
            public function exist($id) {
              $entity = $this->entityQuery->get('lotus')
                ->condition('id', $id)
                ->execute();
              return (bool) $entity;
            }

          }

   #. Add the following code in the
      ``lotus/src/Form/LotusDeleteForm.php`` file:

      .. code-block:: php
         :linenos:

          <?php
          namespace Drupal\lotus\Form;

          use Drupal\Core\Entity\EntityConfirmFormBase;
          use Drupal\Core\Url;
          use Drupal\Core\Form\FormStateInterface;

          /**
          * Builds the form to delete an lotus.
          */
          class LotusDeleteForm extends EntityConfirmFormBase {

            /**
            * {@inheritdoc}
            */
            public function getQuestion() {
              return $this->t('Are you sure you want to delete %name?', array('%name' => $this->entity->label()));
            }

            /**
            * {@inheritdoc}
            */
            public function getCancelUrl() {
              return new Url('entity.lotus.collection');
            }

            /**
            * {@inheritdoc}
            */
            public function getConfirmText() {
              return $this->t('Delete');
            }

            /**
            * {@inheritdoc}
            */
            public function submitForm(array &amp;$form, FormStateInterface $form_state) {
              $this->entity->delete();
              drupal_set_message($this->t('Category %label has been deleted.', array('%label' => $this->entity->label())));

              $form_state->setRedirectUrl($this->getCancelUrl());
            }

          }

Gist Link
---------

https://gist.github.com/gauravgoyal/9023005a3c48919662c0ae2ce37e2a1d

Resources
---------

-  `Create a config
   entity <https://www.drupal.org/docs/8/api/configuration-api/creating-a-configuration-entity-type-in-drupal-8>`__
-  `Configuration / Schema
   metadata <https://www.drupal.org/docs/8/api/configuration-api/configuration-schemametadata>`__
