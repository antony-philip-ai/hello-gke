flowchart LR
    %% ========================
    %% Developer Zone
    %% ========================
    subgraph DEV["Developer Workstation"]
        Dev[Developer]
        Code[Source Code]
        Dev --> Code
    end

    %% ========================
    %% CI/CD Platform
    %% ========================
    subgraph CICD["GitHub CI/CD Platform"]
        Repo[GitHub Repository]
        Action[GitHub Actions]

        subgraph INNER["Inner Loop – Build & Shift-Left Security"]
            SCA[Veracode SCA<br>Dependency Scan]
            SAST_P[Veracode Pipeline Scan<br>Fast SAST]
            Artifact[Build Artifact / Container Image]
        end

        subgraph DEPLOY["Deployment Phase"]
            Deploy[Deploy to Staging]
        end
    end

    %% ========================
    %% Veracode SaaS Platform
    %% ========================
    subgraph VERACODE["Veracode Security Platform (SaaS)"]
        Policy[Policy Engine]
        SAST_Deep[Policy Scan<br>Deep SAST]
        Analytics[Unified Analytics & Reporting]
    end

    %% ========================
    %% Runtime Environment
    %% ========================
    subgraph STAGE["Staging Environment"]
        App[Running Application]
    end

    %% ========================
    %% Outer Loop Security
    %% ========================
    subgraph OUTER["Outer Loop – Runtime Security"]
        DAST[Veracode DAST / ISM]
    end

    %% ========================
    %% Flow Connections
    %% ========================
    Code -->|Commit / Push| Repo
    Repo -->|CI Trigger| Action

    %% Build Security
    Action --> SCA
    Action --> SAST_P
    SCA -->|Dependency Policy Check| Policy
    SAST_P -->|Immediate Feedback| Repo

    %% Deep SAST (Async)
    Action -.->|Async Upload| SAST_Deep
    SAST_Deep -->|Compliance Results| Analytics

    %% Build → Deploy
    Action -->|Build Success| Artifact
    Artifact --> Deploy
    Deploy --> App

    %% DAST Execution
    Deploy -->|Trigger Scan| DAST
    DAST -->|Crawl & Attack| App
    DAST -->|Findings| Analytics

    %% Feedback Loops
    Analytics -->|Metrics / Trends| Repo
    Analytics -->|Risk Posture| Policy
