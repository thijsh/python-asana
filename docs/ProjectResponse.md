# ProjectResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**name** | **str** | Name of the project. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. | [optional] 
**archived** | **bool** | True if the project is archived, false if not. Archived projects do not show in the UI by default and may be treated differently for queries. | [optional] 
**color** | **str** | Color of the project. | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] 
**current_status** | [**ProjectBaseCurrentStatus**](ProjectBaseCurrentStatus.md) |  | [optional] 
**current_status_update** | [**ProjectBaseCurrentStatusUpdate**](ProjectBaseCurrentStatusUpdate.md) |  | [optional] 
**custom_field_settings** | [**list[PortfolioResponseCustomFieldSettings]**](PortfolioResponseCustomFieldSettings.md) | Array of Custom Field Settings (in compact form). | [optional] 
**default_view** | **str** | The default view (list, board, calendar, or timeline) of a project. | [optional] 
**due_date** | **date** | *Deprecated: new integrations should prefer the &#x60;due_on&#x60; field.* | [optional] 
**due_on** | **date** | The day on which this project is due. This takes a date with format YYYY-MM-DD. | [optional] 
**html_notes** | **str** | [Opt In](/docs/inputoutput-options). The notes of the project with formatting as HTML. | [optional] 
**members** | [**list[CustomFieldResponsePeopleValue]**](CustomFieldResponsePeopleValue.md) | Array of users who are members of this project. | [optional] 
**modified_at** | **datetime** | The time at which this project was last modified. *Note: This does not currently reflect any changes in associations such as tasks or comments that may have been added or removed from the project.* | [optional] 
**notes** | **str** | Free-form textual information associated with the project (ie., its description). | [optional] 
**public** | **bool** | True if the project is public to its team. | [optional] 
**start_on** | **date** | The day on which work for this project begins, or null if the project has no start date. This takes a date with &#x60;YYYY-MM-DD&#x60; format. *Note: &#x60;due_on&#x60; or &#x60;due_at&#x60; must be present in the request when setting or unsetting the &#x60;start_on&#x60; parameter. Additionally, &#x60;start_on&#x60; and &#x60;due_on&#x60; cannot be the same date.* | [optional] 
**default_access_level** | **str** | The default access for users or teams who join or are added as members to the project. | [optional] 
**minimum_access_level_for_customization** | **str** | The minimum access level needed for project members to modify this project&#x27;s workflow and appearance. | [optional] 
**minimum_access_level_for_sharing** | **str** | The minimum access level needed for project members to share the project and manage project memberships. | [optional] 
**custom_fields** | [**list[PortfolioResponseCustomFields]**](PortfolioResponseCustomFields.md) | Array of Custom Fields. | [optional] 
**completed** | **bool** | True if the project is currently marked complete, false if not. | [optional] 
**completed_at** | **datetime** | The time at which this project was completed, or null if the project is not completed. | [optional] 
**completed_by** | [**ProjectResponseCompletedBy**](ProjectResponseCompletedBy.md) |  | [optional] 
**followers** | [**list[CustomFieldResponsePeopleValue]**](CustomFieldResponsePeopleValue.md) | Array of users following this project. Followers are a subset of members who have opted in to receive \&quot;tasks added\&quot; notifications for a project. | [optional] 
**owner** | **AllOfProjectResponseOwner** | The current owner of the project, may be null. | [optional] 
**team** | [**ProjectResponseTeam**](ProjectResponseTeam.md) |  | [optional] 
**icon** | **str** | The icon for a project. | [optional] 
**permalink_url** | **str** | A url that points directly to the object within Asana. | [optional] 
**project_brief** | [**ProjectResponseProjectBrief**](ProjectResponseProjectBrief.md) |  | [optional] 
**created_from_template** | [**ProjectResponseCreatedFromTemplate**](ProjectResponseCreatedFromTemplate.md) |  | [optional] 
**workspace** | [**ProjectResponseWorkspace**](ProjectResponseWorkspace.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

