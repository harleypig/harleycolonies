# AI Agents and Automation

This document outlines the AI agents and automation tools available for this
repository, which manages infrastructure using Terraform and Packer, and
service definitions using Docker Compose.

## Agent Overview

This repository supports multiple types of agents for different aspects of
development and infrastructure management:

- **Development Agents** - Code generation, testing, and documentation
- **Infrastructure Agents** - Terraform validation, deployment automation, and
    Packer builds
- **Security Agents** - Scanning, compliance checking, and vulnerability
    assessment
- **Monitoring Agents** - Health checks, alerting, and performance monitoring
- **Style Enforcement Agents** - Code formatting, linting, and consistency
    checking

## General Development Guidelines

- Use clear and descriptive names for resources, variables, and outputs
- Keep modules small and focused on a single responsibility
- Use comments to explain complex logic or decisions
- Commit changes frequently with clear and descriptive commit messages
- Use branches for new features or bug fixes and merge them into the main branch after review
- Document all modules and variables with descriptions
- Provide examples of usage for complex modules or configurations
- **Word Wrapping**: All documentation (markdown files, comments in code,
    plain text files, etc.) must be word wrapped to column 78
- **Branch Management**: When working on features, bug fixes, or todo items,
    automatically create and switch to appropriately named branches:
    - Use `feature/` prefix for new features (e.g., `feature/terraform-module`)
    - Use `bugfix/` prefix for bug fixes (e.g., `bugfix/docker-compose-issue`)
    - Use `refactor/` prefix for code refactoring (e.g., `refactor/terraform-structure`)
    - Use descriptive names that match the todo item or feature being worked on
    - Always create branches from the latest master/main branch
    - Ask for confirmation before switching back to master when work is complete
- **Git Operations**: Follow safe git practices:
    - Use `git add -u` for modified files (preferred over `git add -A`)
    - Explicitly add new files with `git add <filename>` or `git add <directory>`
    - Use `rmdir` when removing directories to catch any missed files
    - Avoid blanket commands like `git add -A` unless specifically needed
    - **Branch Management**: Do not automatically switch back to master branch
      after completing work - give user the chance to reject the switch
    - Always ask for confirmation before switching branches unless explicitly
      requested by the user

## Primary Development Tools

### Aider-Chat Integration

- **Purpose**: AI-powered code generation and modification
- **Usage**: Use `aider-chat` for rapid development and code assistance
- **Configuration**: Follow the patterns established in existing code
- **Best Practices**:
  - Always validate generated code before committing
  - Use descriptive prompts for better results
  - Review changes for security implications

### Cursor CLI Integration

- **Purpose**: AI-assisted development within the Cursor IDE
- **Usage**: Leverage Cursor's AI features for code completion and refactoring
- **Configuration**: Ensure Cursor is configured with appropriate context files
- **Best Practices**:
  - Use Cursor's context awareness features
  - Leverage multi-file editing capabilities
  - Utilize the built-in terminal integration

## MCP (Model Context Protocol) Usage

**Permission**: You have full permission to use MCP tools as needed without
explicit inclusion in prompts.

### Available MCP Tools

- **File Operations**: Read, write, search, and manage files
- **Terminal Commands**: Execute system commands and scripts
- **Web Search**: Research documentation and best practices
- **Library Documentation**: Access up-to-date library documentation
- **Code Analysis**: Perform semantic searches and code analysis

### MCP Best Practices

- Use MCP tools proactively when they can improve the task
- Leverage web search for current documentation and examples
- Use library documentation tools for accurate API references
- Apply file operations for efficient code management

## Development Agents

### Code Generation Agent

- **Purpose**: Generate boilerplate code, configurations, and documentation
- **Scope**: Terraform modules, Docker Compose services, Packer configurations
- **Output**: Well-structured, commented code following repository conventions
- **Validation**: Always includes validation and testing suggestions

### Documentation Agent

- **Purpose**: Auto-generate documentation from code and configurations
- **Features**:
  - Generate README files for modules
  - Create API documentation
  - Update existing documentation
  - Generate architecture diagrams
- **Tools**: Uses `terraform-docs`, custom scripts, and AI generation
- **Conventions**:
  - Document all modules and variables with descriptions
  - Provide examples of usage for complex modules or configurations
  - Use clear and descriptive names for resources, variables, and outputs
  - Use comments to explain complex logic or decisions

### Testing Agent

- **Purpose**: Generate and run tests for infrastructure code
- **Coverage**:
  - Terraform validation and testing
  - Docker Compose service testing
  - Packer build validation
  - Integration testing
- **Framework**: Follows patterns in `TESTS.md`

## Infrastructure Agents

### Terraform Agent

- **Purpose**: Manage Terraform configurations and deployments
- **Capabilities**:
  - Validate configurations (`terraform validate`)
  - Format code (`terraform fmt`)
  - Generate plans
  - Does not apply changes (`terraform apply`)
  - Manage state files
  - Generate documentation
- **Modules**: Supports all modules in `tfmods/`, `domains/`, `servers/`, `volumes/`
- **Backend**: Integrates with S3-compatible Linode storage
- **Conventions**:
  - Use `terraform fmt` to format code consistently
  - Organize resources by type and purpose
  - Use variables for configurable values and provide default values where appropriate
  - Use outputs to expose necessary information from modules
  - Keep modules small and focused on a single responsibility

### Packer Agent

- **Purpose**: Manage golden image builds
- **Capabilities**:
  - Validate Packer configurations (`packer validate`)
  - Format Packer files (`packer fmt`)
  - Build golden images
  - Manage build artifacts
- **Configuration**: Uses `golden-image/` directory structure
- **Conventions**:
  - Use `packer fmt` to format code consistently
  - Define variables for all user-configurable settings
  - Use provisioners to automate configuration tasks
  - Keep build scripts idempotent to ensure consistent results

### Docker Agent

- **Purpose**: Manage Docker Compose services and containers
- **Capabilities**:
  - Validate Docker Compose configurations
  - Manage service deployments
  - Handle SSL/TLS certificates (Let's Encrypt)
  - Monitor container health
- **Services**: Traefik, Authelia, Redis, static web pages
- **Environments**: Test, QA, Production

## Security Agents

### Vulnerability Scanning Agent

- **Purpose**: Scan for security vulnerabilities
- **Tools**:
  - [CIS Docker Benchmark](https://github.com/dev-sec/cis-docker-benchmark)
  - [Checkov](https://github.com/bridgecrewio/checkov)
  - [Docker Bench Security](https://github.com/docker/docker-bench-security)
  - [KICS](https://github.com/checkmarx/kics)
  - [Syft](https://github.com/anchore/syft)
- **Scope**: Docker images, Terraform configurations, system hardening

### Compliance Agent

- **Purpose**: Ensure compliance with security standards
- **Standards**: CIS benchmarks, security best practices
- **Reporting**: Generates compliance reports and remediation suggestions

## Style Enforcement Agents

### Code Formatting Agent

- **Purpose**: Enforce consistent code formatting
- **Tools**:
  - `terraform fmt` for Terraform files
  - `packer fmt` for Packer files
  - Prettier for documentation files
  - Shell script formatting (`shfmt`)
- **Automation**: Runs automatically on commit via pre-commit hooks

### Linting Agent

- **Purpose**: Enforce coding standards and best practices
- **Tools**:
  - Terraform linting (tflint)
  - Shell script linting (shellcheck)
  - YAML linting (yamllint)
  - Dockerfile linting
- **Rules**: Follows conventions defined in this document

### Naming Convention Agent

- **Purpose**: Enforce consistent naming across all resources
- **Standards**:
  - Clear and descriptive names
  - Consistent naming patterns
  - Proper resource organization
- **Scope**: Terraform resources, Docker services, file names

## Monitoring Agents

### Health Check Agent

- **Purpose**: Monitor service health and availability
- **Services**: All Docker Compose services
- **Metrics**: Response times, error rates, resource usage
- **Alerting**: Configurable alerts for service failures

### Performance Monitoring Agent

- **Purpose**: Monitor system and application performance
- **Tools**: Traefik metrics, container stats, system resources
- **Reporting**: Performance reports and optimization suggestions

## Version Control

### Git Workflow Agent

- **Purpose**: Enforce consistent version control practices
- **Conventions**:
  - Commit changes frequently with clear and descriptive commit messages
  - Use branches for new features or bug fixes and merge them into the main branch after review
  - Follow conventional commit message format when possible
  - Ensure all commits are properly signed and verified
- **Automation**:
  - Pre-commit hooks for formatting and linting
  - Automated testing on pull requests
  - Branch protection rules for main branch

## Configuration and Setup

### Environment Variables

Agents use environment variables defined in:
- `env` files for Docker services
- `set_env` script for Terraform operations
- System environment variables

### Required Tools

- Docker and Docker Compose
- Terraform CLI
- Packer CLI
- Git
- Shell scripting tools

### Agent Permissions

- Full read/write access to repository files
- Execute system commands as needed
- Access to external APIs and documentation
- MCP tool usage without explicit permission requests

## Usage Examples

### Development Workflow

```bash
# Start development session with aider-chat
aider-chat

# Use Cursor CLI for IDE integration
cursor-agent .

# Generate documentation
bin/build-docs

# Run style enforcement
terraform fmt
packer fmt
```

### Infrastructure Management

```bash
# Initialize Terraform with backend
. set_env
cd domains/
terraform init -backend-config=domains.s3.tfbackend

# Validate and plan
terraform validate
terraform plan

# Apply changes (agent should not run)
terraform apply
```

### Security Scanning

```bash
# Run Docker security scan
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy image <image-name>

# Run Terraform security scan
checkov -d .
kics .
```

## Best Practices

### Agent Interaction

- Always validate agent-generated code
- Review security implications of changes
- Test changes in development environment first
- Follow established naming conventions
- Maintain documentation consistency

### Error Handling

- Agents should provide clear error messages
- Include remediation suggestions
- Log all agent activities
- Graceful degradation on tool failures

### Performance

- Use parallel execution where possible
- Cache results when appropriate
- Optimize for common use cases
- Monitor agent performance

## Troubleshooting

### Common Issues

- **Terraform Backend Issues**: Check S3 configuration and credentials
- **Docker Service Failures**: Check logs with `docker logs <container>`
- **Certificate Issues**: Verify Let's Encrypt or mkcert configuration
- **Agent Permission Issues**: Ensure proper environment setup

### Debugging Commands

```bash
# Check Terraform state
terraform show

# Check Docker service status
docker-compose ps

# View service logs
docker logs <service-name>

# Validate configurations
terraform validate
packer validate .
```

## Contributing

When adding new agents or modifying existing ones:
1. Follow the established patterns
2. Update this documentation
3. Include appropriate tests
4. Ensure security considerations
5. Maintain backward compatibility

## Resources

- [Terraform Documentation](https://developer.hashicorp.com/terraform/docs)
- [Packer Documentation](https://developer.hashicorp.com/packer/docs)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [CIS Benchmarks](https://www.cisecurity.org/benchmarks/)
- [Aider Documentation](https://aider.chat/)
- [Cursor Documentation](https://cursor.sh/docs)
