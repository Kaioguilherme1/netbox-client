#customization
::: customization

subclasses of customization

```mermaid
graph TD;
    A[netboxcli] --> B[core];
    B --> D;
    A --> C[Client];
    C --> D[customization];
    D --> E[custom_fields];
    D --> F[custom_links];
    D --> G[export_templates];
    D --> H[image_attachments];
    D --> I[reports];
    D --> J[scripts];
    D --> K[saved_filters];
    D --> L[tags];
```