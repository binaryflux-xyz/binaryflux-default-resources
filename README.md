# BinaryFlux Default Resources

This repository contains default resources that are automatically loaded during system initialization. These resources include predefined configurations, contents that are essential for the BinaryFlux platform to function correctly.

## Purpose

The default resources ensure that the system has all necessary configurations and permissions set up out-of-the-box. This includes:

- Predefined security roles and permissions
- Default workflow definitions
- System configurations
- Other essential resources required for initial setup

## Directory Structure

It is crucial to maintain the following directory structure for proper resource loading:

```
binaryflux-default-resources/
├── config/                    # Configuration files (binaryflux-configuration-service will handle this resource)
│   └── securityrole/         # kind: securityrole
│       └── standardRoles.json # Default security roles and permissions
└── content/                  # Content-related resources (content-repository-service will handle this resource)
    └── workflows/            # contenttype: workflow
        ├── message_en.properties    # Example workflow definition
        └── script.py    # Example workflow definition
```

## Adding New Resources

When adding new default resources:

1. Place configuration files in the appropriate subdirectory under `config/`
2. Place content-related resources in the appropriate subdirectory under `content/`
3. Follow the existing naming conventions and file formats
4. Update this README if you add new directory types

## Loading Mechanism

These resources are automatically loaded during system startup by the configuration service. The system will:

1. Scan the configured directories
2. Validate each resource
3. Load them into the appropriate services
4. Skip any resources that already exist (based on unique identifiers)

## Best Practices

- Keep resource files well-documented with comments
- Use descriptive filenames that reflect their purpose
- Follow the JSON schema defined for each resource type
- Test new resources in a development environment before committing
- Document any dependencies between resources

## Versioning

This repository follows semantic versioning. When making changes to default resources:

- Increment the patch version for backward-compatible bug fixes
- Increment the minor version for adding resources in a backward-compatible way
- Increment the major version for incompatible changes

## License

[Specify License Information]
