flowchart TD
    %% Define Nodes
    subgraph "Developer Workstation"
        Dev[Developer]
        Code[Source Code]
    end

    subgraph "GitHub (CI/CD)"
        Repo[GitHub Repository]
        Action[GitHub Actions Workflow]
        
        subgraph "Build Phase (Inner Loop)"
            SCA[Veracode SCA<br/>(Dependency Scan)]
            SAST_P[Veracode Pipeline Scan<br/>(Fast SAST)]
            Artifact[Build Artifact / Container]
        end
        
        subgraph "Deployment Phase"
            Deploy[Deploy to Staging]
        end
    end

    subgraph "Veracode Platform"
        Policy[Policy Engine]
        Analytics[Unified Reporting]
        SAST_Deep[Policy Scan<br/>(Deep SAST)]
    end

    subgraph "Staging Environment"
        App[Running Application]
    end

    subgraph "Dynamic Analysis (Outer Loop)"
        DAST[Veracode DAST / ISM]
    end

    %% Define Edges
    Dev -->|Commit/Push| Repo
    Repo -->|Trigger| Action
    
    %% Build Steps
    Action --> SCA
    Action --> SAST_P
    SCA -->|Manifest Check| Policy
    SAST_P -->|Pass/Fail Feedback| Repo
    
    %% Deep Scan Async
    Action -.->|Async Upload| SAST_Deep
    SAST_Deep -->|Compliance Report| Analytics

    %% Deployment & DAST
    Action -->|Success| Artifact
    Artifact --> Deploy
    Deploy --> App
    Deploy -->|Trigger Event| DAST
    
    %% DAST Execution
    DAST -->|Crawl & Attack| App
    DAST -->|Results| Analytics

    %% Feedback Loops
    Analytics -->|Aggregated Metrics| Repo
    SCA -->|Issues/PR Comments| Repo
