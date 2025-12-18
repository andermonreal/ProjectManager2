INSERT INTO users
(name, email, password, phone, birthday, money, icon, is_active, is_staff, is_superuser, last_login)
VALUES
-- Superusers (máximo 5)
('andoni', 'andoni@projectManager.com', 'dbcfa902fd131b8a9fa28e045367a8ccb0eabd89', '600222222', '1988-03-15', 0.00, '', TRUE, TRUE, TRUE, NULL),
('ander', 'ander@projectManager.com', '3182c8e8bccbf13f48fd110da789a0420206a3d8', '600333333', '1985-07-20', 0.00, '', TRUE, TRUE, TRUE, NULL),
('elisabeth', 'elisabeth@projectManager.com', '6453fb05855c8e275d0a8fcb1dbd946ea0b8fc9e', '600444444', '1992-11-05', 0.00, '', TRUE, TRUE, TRUE, NULL),
('monre', 'monre@projectManager.com', 'a761ce3a45d97e41840a788495e85a70d1bb3815', '600111111', '1990-01-10', 0.00, '', TRUE, TRUE, TRUE, NULL),
('tomi', 'tomi@projectManager.com', '62697ba227ef69776af46c700749bfbc99f5ffcb', '600555555', '1995-09-25', 0.00, '', TRUE, TRUE, TRUE, NULL),

-- Usuarios normales
('alex', 'alex@projectManager.com', 'cbfdac6008f9cab4083784cbd1874f76618d2a97', '610000001', '1995-02-02', 10.50, '', TRUE, TRUE, FALSE, NULL),
('carla', 'carla.santos@projectManager.com', '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8', '610000002', '1993-04-12', 5.00, '', TRUE, FALSE, FALSE, NULL),
('jose', 'jose.rodriguez@projectManager.com', '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed', '610000003', '1991-06-23', 0.00, '', TRUE, FALSE, FALSE, NULL),
('andrea', 'andrea.pm@projectManager.com', '8cb2237d0679ca88db6464eac60da96345513964', '610000004', '1994-08-30', 100.00, '', TRUE, TRUE, FALSE, NULL),
('maria', 'maria.gomez@projectManager.com', '7b52009b64fd0a2a49e6d8a939753077792b0554', '610000005', '1990-12-01', 0.00, '', TRUE, FALSE, FALSE, NULL),

('ricardo', 'ricardo.luna@projectManager.com', '4a7d1ed414474e4033ac29ccb8653d9b', '610000006', '1989-10-10', 50.00, '', TRUE, FALSE, FALSE, NULL),
('isabel', 'isabel@projectManager.com', '5d41402abc4b2a76b9719d911017c592', '610000007', '1992-01-19', 0.00, '', TRUE, FALSE, FALSE, NULL),
('mariano', 'mariano.pm@projectManager.com', 'b0baee9d279d34fa1dfd71aadb908c3f', '610000008', '1988-05-09', 0.00, '', TRUE, TRUE, FALSE, NULL),
('ana', 'ana.fernandez@projectManager.com', '2fd4e1c67a2d28fced849ee1bb76e7391b93eb12', '610000009', '1996-03-03', 12.75, '', TRUE, FALSE, FALSE, NULL),
('mark', 'mark.jones@projectManager.com', 'a9993e364706816aba3e25717850c26c9cd0d89d', '610000010', '1991-07-17', 0.00, '', TRUE, FALSE, FALSE, NULL),

('paula', 'paula.castillo@projectManager.com', 'da39a3ee5e6b4b0d3255bfef95601890afd80709', '610000011', '1993-09-09', 0.00, '', TRUE, FALSE, FALSE, NULL),
('david', 'david.sanchez@projectManager.com', 'c1dfd96eea8cc2b62785275bca38ac261256e278', '610000012', '1990-10-21', 3.20, '', TRUE, TRUE, FALSE, NULL),
('equipo', 'equipo@projectManager.com', 'e242ed3bffccdf271b7fbaf34ed72d089537b42f', '610000013', '2000-01-01', 0.00, '', TRUE, FALSE, FALSE, NULL),
('soporte', 'soporte@projectManager.com', '3de8f8b0dc94b8c2230fab9ec0ba0506', '610000014', '1998-11-11', 0.00, '', TRUE, TRUE, FALSE, NULL),
('gestion', 'gestion.proyectos@projectManager.com', '9c1185a5c5e9fc54612808977ee8f548b2258d31', '610000015', '1997-04-04', 0.00, '', TRUE, TRUE, FALSE, NULL),

('coordinacion', 'coordinacion@projectManager.com', '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33', '610000016', '1992-02-20', 0.00, '', TRUE, FALSE, FALSE, NULL),
('contacto', 'contacto@projectManager.com', '4b825dc642cb6eb9a060e54bf8d69288fbee4904', '610000017', '1994-06-06', 0.00, '', TRUE, FALSE, FALSE, NULL),
('proyectos', 'proyectos@projectManager.com', '1f8ac10f23c5b5bc1167bda84b833e5c057a77d2', '610000018', '1993-03-13', 0.00, '', TRUE, TRUE, FALSE, NULL),
('reclutamiento', 'reclutamiento@projectManager.com', '8f14e45fceea167a5a36dedd4bea2543', '610000019', '1991-09-19', 0.00, '', TRUE, FALSE, FALSE, NULL),
('marketing', 'marketing@projectManager.com', '45c48cce2e2d7fbdea1afc51c7c6ad26', '610000020', '1990-05-05', 0.00, '', TRUE, FALSE, FALSE, NULL),

('ventas', 'ventas@projectManager.com', '6512bd43d9caa6e02c990b0a82652dca', '610000021', '1989-08-08', 0.00, '', TRUE, FALSE, FALSE, NULL),
('asistente', 'asistente@projectManager.com', 'c20ad4d76fe97759aa27a0c99bff6710', '610000022', '1995-12-12', 0.00, '', TRUE, FALSE, FALSE, NULL),
('planificacion', 'planificacion@projectManager.com', 'c51ce410c124a10e0db5e4b97fc2af39', '610000023', '1996-07-07', 0.00, '', TRUE, FALSE, FALSE, NULL),
('finanzas', 'finanzas@projectManager.com', 'a87ff679a2f3e71d9181a67b7542122c', '610000024', '1987-01-27', 0.00, '', TRUE, TRUE, FALSE, NULL),
('direccion', 'direccion@projectManager.com', 'e4da3b7fbbce2345d7772b0674a318d5', '610000025', '1985-02-14', 0.00, '', TRUE, TRUE, FALSE, NULL);

INSERT INTO projects (user_id, title, description, content)
VALUES
(1,
 'Enterprise Resource Planning Rollout',
 'Phased implementation of an ERP platform across all departments.',
 'This project covers the complete rollout of an enterprise resource planning (ERP) platform across finance, operations, HR, and sales. The content includes a detailed breakdown of phases, starting with discovery and requirements gathering, moving into data modeling, integration design, user acceptance testing, and final cutover.
 The document describes all stakeholders involved, their responsibilities, and the communication plan for each phase. It explains how existing legacy systems will be audited, which data will be migrated, how data cleansing will be performed, and which validation rules will be applied before and after migration.
 It also includes extensive notes on risk management, such as how to handle partial failures during migration, fallback procedures, and contingency planning. The project content goes deeper into training plans, including creation of training materials, scheduling of workshops, office hours for support, and a feedback loop to continuously improve training sessions.
 Additionally, the project outlines performance KPIs like system adoption rate, reduction in manual work, error rates in financial reports, and time to close monthly books. Each KPI is tied to specific tasks, responsible owners, and reporting cadences. The content finally explains post‑go‑live stabilization activities, continuous improvement backlog, and governance structures that will keep the ERP platform aligned with evolving business needs.'
),

(2,
 'Customer Relationship Management Consolidation',
 'Unify multiple CRM tools into a single platform with standardized processes.',
 'This project aims to consolidate several disparate customer relationship management (CRM) tools used by different teams into a unified, company‑wide platform. The content explains the current fragmented landscape, where sales, marketing, and customer support each maintain separate databases and overlapping workflows.
 The document details how the new platform will become the single source of truth for customer records, interactions, opportunities, support tickets, and marketing activities. It describes the mapping of fields between legacy systems and the new CRM, the transformation rules that will be applied, and the order in which data sets will be migrated.
 A complete playbook for process standardization is included, covering lead qualification, opportunity stages, handoffs between marketing and sales, and escalation rules for high‑value accounts. The project content discusses how automation will be configured to send alerts, assign tasks, and create follow‑up activities based on business rules.
 It also includes long narrative sections about change management: how stakeholders will be identified, how champions inside each department will be empowered, and how feedback will be collected after every iteration of the rollout. Training modules will be designed for different roles, such as sales reps, managers, and administrators, with progressively advanced content.
 Finally, the project describes a robust reporting framework, with dashboards for pipeline health, conversion rates, campaign performance, and customer retention. These dashboards will be reviewed regularly in leadership meetings, and the project content specifies which decisions should be informed by which metrics, ensuring the new CRM directly supports strategic planning.'
),

(3,
 'Data Warehouse Modernization Initiative',
 'Rebuild the data warehouse to support analytics and self‑service BI.',
 'The Data Warehouse Modernization Initiative focuses on redesigning the existing analytical environment to support modern self‑service business intelligence and scalable data processing. The content starts with an in‑depth description of current pain points: slow queries, inconsistent metrics, duplicate reports, and limited access for non‑technical users.
 It then introduces a target architecture based on a layered approach, separating raw ingestion, standardized data models, and curated data marts for specific domains such as finance, sales, product, and operations. The document explains how batch and near real‑time ingestion pipelines will be implemented, including change data capture, event streaming, and API‑based extractions from third‑party systems.
 The project content provides a detailed description of dimensional modeling practices, such as star schemas, slowly changing dimensions, and conformed dimensions to ensure that metrics like revenue, active users, and churn are consistently defined across the organization. It also discusses governance practices, including a data catalog, business glossaries, and stewardship roles for key datasets.
 A large section is dedicated to performance and cost optimization strategies: partitioning and clustering of large tables, indexing policies, workload management, and the use of resource groups or query queues to protect critical dashboards from ad‑hoc heavy queries. Security and compliance are addressed through row‑level and column‑level access controls, encryption, and auditing configurations.
 Finally, the initiative outlines a comprehensive enablement plan to encourage self‑service analytics. This includes office hours, open forums, documentation sprints, and curated examples of dashboards that demonstrate best practices for visualization, storytelling with data, and interpretability. The project content stresses continuous improvement, with a backlog of enhancements driven by feedback from analysts and business users.'
),

(4,
 'Mobile Application for Field Technicians',
 'Design and develop a mobile app to support technicians working on‑site.',
 'This project describes the end‑to‑end development of a mobile application to support field technicians who perform installations, repairs, and inspections on customer sites. The content begins with personas and user journeys that illustrate how technicians prepare for a visit, travel, execute tasks, capture information, and close work orders.
 The project text goes into significant detail about offline‑first behavior, explaining how the app must continue to function in areas with limited or no connectivity. It specifies caching strategies, synchronization intervals, conflict resolution rules when multiple edits are made offline, and the visual indicators that will inform technicians about sync status.
 The requirements section outlines core features: viewing daily schedules, accessing step‑by‑step procedures, capturing photos and videos, scanning barcodes or QR codes on equipment, logging consumed parts, and obtaining digital signatures from customers. Each feature is accompanied by acceptance criteria and edge cases to be tested.
 The content also defines non‑functional requirements such as performance targets, supported devices, operating systems, accessibility standards, and security constraints. It dedicates several paragraphs to security measures like device‑level encryption, secure storage of credentials, and revocation of access when a device is lost or an employee leaves the company.
 In addition, the project covers integration with the backend system that manages work orders, inventory, and customer history. It describes API contracts, error handling, retry behavior, and monitoring. Finally, it includes a phased rollout plan, starting with a pilot group of technicians, their feedback loops, and the metrics that will be used to determine readiness for broader deployment across the organization.'
),

(5,
 'Customer Self‑Service Knowledge Base',
 'Create a comprehensive self‑service portal to reduce support volume.',
 'The objective of this project is to design and implement a customer self‑service knowledge base that significantly reduces the volume of repetitive support requests. The content provides a thorough overview of the current support workload, categorizing tickets by topic, complexity, and the channels through which they arrive.
 A large section details the information architecture of the knowledge base, including top‑level categories, subcategories, and navigational elements like related articles, breadcrumbs, and search filters. It explains how content will be written in a consistent tone, with clear step‑by‑step instructions, screenshots, and short videos where appropriate.
 The project text lays out a content lifecycle: article creation, technical review, editorial review, publication, periodic review, and eventual deprecation or merging. It specifies ownership models, SLAs for updating articles after product changes, and a tagging system to analyze which content is most consumed and which gaps remain.
 Search optimization is another essential part of the content. It describes keyword strategies, synonyms, and how search logs will be mined to identify common phrases that do not yet yield helpful results. The project describes how customer feedback tools like article ratings and comments will drive continuous improvement of documentation.
 Furthermore, the project discusses integration with the ticketing system so that support agents can link knowledge base articles directly into responses and suggest new article candidates for recurring issues. The content ends with measurable goals such as target deflection rates, average time to solution for self‑service users, and improved satisfaction scores, along with reporting methods to track these outcomes.'
),

(6,
 'Company‑Wide OKR Implementation',
 'Introduce Objectives and Key Results methodology across all teams.',
 'This project aims to introduce the Objectives and Key Results (OKR) methodology across the entire organization. The content explains the rationale for adopting OKRs, highlighting the need for better alignment, clearer prioritization, and more transparent tracking of outcomes rather than output.
 It describes a multi‑wave rollout approach, beginning with an executive training session that establishes a common understanding of what good objectives and key results look like. The project text walks through examples of well‑phrased objectives that are qualitative and inspirational, paired with key results that are specific, measurable, and time‑bound.
 A substantial portion of the content focuses on the practical mechanics of OKRs: the quarterly cadence, how teams should draft proposals, how conflicts between teams will be resolved, and how dependencies will be surfaced early. It explains the review rituals, including mid‑quarter check‑ins and end‑of‑quarter retrospectives, along with the types of questions that should guide these conversations.
 The project also defines roles such as OKR champions in each department, whose responsibility is to coach teammates on writing effective OKRs and to flag misalignments before they impact execution. It includes sample templates, checklists, and examples of anti‑patterns such as using tasks instead of outcomes or setting too many key results.
 Finally, the project discusses tooling options for tracking OKRs, whether through dedicated platforms or structured documents and dashboards. It defines how progress will be visualized, how commentary will be captured, and how learnings from each cycle will feed into continuous improvements of the methodology so that OKRs become a natural part of planning rather than an administrative burden.'
),
(1, 'Admin Reporting Overhaul', 'Redesign of all admin reports.', 'Project to centralize and standardize admin reports, aligning metrics with leadership needs and reducing manual spreadsheet work.'),
(1, 'Compliance Documentation Refresh', 'Update of security and compliance docs.', 'Review of all compliance documents, aligning them with current processes and tools, and preparing for upcoming audits.'),

(2, 'Inbound Lead Workflow', 'Standard inbound lead handling.', 'Definition of a clear path from new lead to qualified opportunity, including SLAs and automation rules for the marketing team.'),
(2, 'Social Media Campaign Calendar', 'Calendar for social posts.', 'Creation of a structured calendar for campaigns, approvals, and performance tracking across all social channels.'),

(3, 'Customer Segmentation Model', 'Segment customers by value and behavior.', 'Build a segmentation model to group customers based on value, engagement, and product usage patterns.'),
(3, 'Renewal Playbook', 'Playbook for contract renewals.', 'Define steps, timelines, and communication templates to manage renewals and reduce churn.'),

(4, 'Field App Bug Triage', 'Process for triaging mobile app bugs.', 'Establish weekly triage sessions, priorities, and ownership for bugs reported by field technicians.'),
(4, 'Technician Training Program', 'Training program for new technicians.', 'Design curriculum, materials, and schedules for onboarding new field staff to tools and procedures.'),

(5, 'Financial Forecasting Tool', 'Tool to improve forecasting.', 'Create a forecasting model and dashboard for revenue, costs, and cash flow, integrated with accounting data.'),
(5, 'Expense Review Automation', 'Automate recurring expense review.', 'Set up rules and workflows to automatically flag unusual expenses for manual review.'),

(6, 'User Onboarding Emails', 'Automated onboarding email series.', 'Define and implement a multi‑step onboarding email journey for new users of the platform.'),
(6, 'Churn Risk Alerts', 'Alerts for at‑risk accounts.', 'Create logic and notifications to flag users with high churn risk based on activity and support interactions.'),

(7, 'Support SLA Dashboard', 'Dashboard for support SLAs.', 'Build a real‑time dashboard showing SLA performance for all support queues and teams.'),
(7, 'Ticket Tagging Guidelines', 'Standardize support ticket tags.', 'Document and train the team on a unified tagging scheme for cases to improve reporting accuracy.'),

(8, 'Internal HR Surveys', 'Recurring internal engagement surveys.', 'Design survey templates, cadence, and reporting flow for measuring employee engagement.'),
(8, 'Benefits Portal Content', 'Content for the benefits portal.', 'Prepare clear explanations of benefits, FAQs, and guidance on how to request changes.'),

(9, 'CRM Opportunity Hygiene', 'Improve data quality on opportunities.', 'Define rules and checks for stages, amounts, and close dates in the CRM to increase forecast accuracy.'),
(9, 'Account Assignment Rules', 'Rules for account ownership.', 'Implement assignment logic and documentation for shared and strategic accounts.'),

(10, 'Email Domain Warmup', 'Warm up new sending domain.', 'Plan and execute a sending schedule to warm up a new email domain and preserve deliverability.'),
(10, 'Newsletter Redesign', 'Redesign monthly newsletter.', 'Update layout, sections, and calls to action of the main company newsletter.'),

(11, 'Security Incident Runbooks', 'Runbooks for security incidents.', 'Draft, review, and publish runbooks for common incident patterns with clear responsibilities.'),
(11, 'Password Policy Rollout', 'Rollout of new password policy.', 'Communicate, implement, and monitor new password complexity and rotation requirements.'),

(12, 'Staging Environment Standardization', 'Standardize staging environments.', 'Align staging environments across teams, including data sets, configuration, and access rules.'),
(12, 'Deployment Checklist', 'Standard deployment checklist.', 'Create a simple but complete checklist for each release, shared across dev and ops teams.'),

(13, 'Customer Advisory Board', 'Launch a customer advisory board.', 'Define membership, meeting cadence, and topics for a recurring advisory board with key clients.'),
(13, 'Reference Customer Program', 'Program for reference customers.', 'Identify, onboard, and support customers willing to act as references and provide case studies.'),

(14, 'API Documentation Portal', 'Portal for API docs.', 'Create a developer‑friendly documentation site with examples, reference pages, and changelog.'),
(14, 'Webhook Reliability Improvements', 'Improve webhook delivery.', 'Add retries, dead‑letter queues, and better logging around outbound webhook delivery.'),

(15, 'Partner Certification Path', 'Certification for partners.', 'Design training and exams for partners to become certified implementers of the product.'),
(15, 'Co‑Marketing Guidelines', 'Guidelines for co‑marketing.', 'Document process, requirements, and templates for joint marketing activities with partners.'),

(16, 'Editorial Review Workflow', 'Workflow for content review.', 'Set up a multi‑step review system for blog posts, landing pages, and documentation.'),
(16, 'Brand Asset Library', 'Central library of brand assets.', 'Organize logos, templates, photos, and examples into a single, searchable location.'),

(17, 'Quarterly OKR Templates', 'Templates for OKRs.', 'Provide ready‑to‑use templates with examples for teams to define quarterly OKRs.'),
(17, 'Leadership Review Rhythm', 'Rhythm for OKR reviews.', 'Define monthly and quarterly leadership review meetings focused on progress against OKRs.'),

(18, 'Manager Feedback Toolkit', 'Toolkit for managers', 'Create resources, examples, and guidelines to help managers give structured feedback to their reports.'),
(18, 'Learning Paths Catalog', 'Catalog of learning paths.', 'Group training resources into clear learning paths by role and seniority level.'),

(19, 'Tracking Plan for New Features', 'Events for new product modules.', 'Define events and properties to track behavior across all recently launched modules.'),
(19, 'Standard KPI Definitions', 'Standardize KPI definitions.', 'Document canonical definitions for revenue, active users, churn, and other core metrics.'),

(20, 'Homepage A/B Experiments', 'Test variations on homepage.', 'Design and execute several experiments on the homepage hero, CTA, and social proof sections.'),
(20, 'Blog Migration to New CMS', 'Migrate blog content.', 'Export, transform, and import all blog posts, and validate URLs and redirects.'),

(21, 'Budget vs Actuals Dashboard', 'Dashboard for budget tracking.', 'Create visual comparisons between planned and actual spend, by department and category.'),
(21, 'Invoice Reminder Workflow', 'Automatic invoice reminders.', 'Set up email and in‑app reminders for overdue invoices with different escalation levels.'),

(22, 'Internal Communication Guidelines', 'Guidelines for internal comms.', 'Define channels, tone, and timing rules for announcements and project updates.'),
(22, 'Meeting Hygiene Initiative', 'Improve meeting practices.', 'Introduce agenda templates, note‑taking norms, and decision logs for recurring meetings.'),

(23, 'Incident Severity Matrix', 'Define severity levels.', 'Create a matrix that maps incident characteristics to standardized severity levels.'),
(23, 'Post‑Incident Review Portal', 'Portal for incident reviews.', 'Centralize documentation and follow‑up tasks for each major incident.'),

(24, 'Release Calendar Publication', 'Publish release calendar.', 'Maintain a shared calendar with upcoming releases, freeze periods, and key milestones.'),
(24, 'Feature Flag Naming Rules', 'Rules for feature flag names.', 'Create guidelines for flag names, lifecycles, and ownership.'),

(25, 'Localization QA Checklist', 'Checklist for localized features.', 'Prepare checklist items for UI, formats, and content verification in each supported language.'),
(25, 'Regional Launch Playbook', 'Playbook for regional launches.', 'Describe steps for launching in a new region, including legal, marketing, and support.'),

(6, 'Beta Program for Power Users', 'Beta program structure.', 'Identify power users, invite them to early access programs, and define feedback loops.'),
(7, 'Knowledge Base Cleanup', 'Cleanup of old articles.', 'Archive or merge outdated support content and refresh the most visited pages.'),
(8, 'Employee Handbook Update', 'Update employee handbook.', 'Incorporate new policies, remote work rules, and updated benefits into the handbook.'),
(9, 'Cross‑Sell Playbook', 'Playbook for cross‑selling.', 'Define triggers, scripts, and follow‑up actions for cross‑selling opportunities.'),
(10, 'Transactional Email Review', 'Review transactional emails.', 'Audit all system emails and improve clarity, branding, and tracking.'),
(11, 'Access Review Automation', 'Automate quarterly access review.', 'Create reports and workflows for reviewing user permissions on a recurring basis.'),
(12, 'Environment Cost Monitoring', 'Monitor infra costs.', 'Add dashboards and alerts to track infrastructure spend across environments.'),
(13, 'Strategic Account Plans', 'Plans for strategic accounts.', 'Create account plans covering goals, risks, and expansion opportunities.'),
(14, 'SDK Example Gallery', 'Gallery of SDK examples.', 'Build a collection of small, focused examples for developers using the SDK.'),
(15, 'Partner Deal Registration', 'Deal registration process.', 'Implement a form and workflow to register partner‑sourced deals.'),
(16, 'Content Refresh Initiative', 'Refresh old content.', 'Identify and update older content pieces that still receive traffic.'),
(17, 'OKR Coaching Sessions', 'Coaching program for OKRs.', 'Schedule and run coaching sessions for teams struggling with OKR adoption.'),
(18, 'Onboarding for New Managers', 'New manager onboarding.', 'Build a structured onboarding track for people who become managers.'),
(19, 'Experiment Results Repository', 'Central repository for tests.', 'Store outcomes, learnings, and decisions from product and growth experiments.'),
(20, 'SEO Content Cluster Build', 'Build content clusters.', 'Create topic clusters and pillar pages to strengthen SEO authority.'),
(21, 'Finance Policy Wiki', 'Wiki for finance policies.', 'Document guidelines for purchasing, reimbursements, and approvals.'),
(22, 'Async Communication Playbook', 'Playbook for async work.', 'Promote asynchronous work practices with examples and tools.'),
(23, 'Incident Drill Schedule', 'Schedule for drills.', 'Plan and execute incident response drills each quarter.'),
(24, 'Canary Release Strategy', 'Strategy for canary releases.', 'Define how small canary groups will be used to validate releases.'),
(25, 'Translation Memory Setup', 'Set up translation memory.', 'Configure translation memory tools and workflows for efficiency.'),

(1, 'Internal Management Dashboard', 'Core dashboard for admins.', 'Long internal content about KPIs, charts, role-based widgets and alerts.'),
(1, 'User Role Refactor', 'Refactor of permission system.', 'Detailed description of how to migrate from legacy roles to a granular permission model.'),

(2, 'Marketing Campaign Q1', 'Digital marketing plan for Q1.', 'Full funnel definition, channels, budget allocation and performance indicators.'),
(2, 'SEO Optimization Sprint', 'Technical SEO tasks.', 'Backlog including metadata fixes, sitemap review, and performance improvements.'),

(3, 'Client Portal Redesign', 'New UX for the client portal.', 'Information architecture, wireframes and content strategy for the new portal.'),
(3, 'Billing Automation', 'Automate invoices and reminders.', 'Workflow description with triggers, email templates and integration points.'),

(4, 'Mobile App MVP', 'Initial mobile application MVP.', 'Scope, user stories and acceptance criteria for the first mobile release.'),
(4, 'Push Notification System', 'Notification service for the app.', 'Architecture notes, retry logic and segmentation rules.'),

(5, 'Data Warehouse Setup', 'Initial DW on cloud.', 'Star schema definition, ETL processes and data quality checks.'),
(5, 'Reporting Suite', 'Business reports for management.', 'Set of dashboards with revenue, churn and acquisition metrics.'),

(6, 'Onboarding Flow', 'Improve user onboarding.', 'Step-by-step onboarding, email drips and in-app guidance.'),
(6, 'Feedback Collection', 'Centralize user feedback.', 'Form designs, tagging strategy and reporting for feedback items.'),

(7, 'Support Center Migration', 'Move support center to new tool.', 'Migration steps, data export/import and redirect mapping.'),
(7, 'Knowledge Base Expansion', 'Add new articles.', 'List of required topics, owners and review schedule.'),

(8, 'HR Portal', 'Portal for internal HR processes.', 'Modules for vacations, evaluations and internal communication.'),
(8, 'Recruitment Pipeline', 'Track candidates and openings.', 'Stages, automations and reporting for recruitment.'),

(9, 'Sales CRM Integration', 'Integrate CRM with platform.', 'Field mapping, sync strategy and error handling.'),
(9, 'Lead Scoring Model', 'Score incoming leads.', 'Rules and scoring weights for marketing and sales teams.'),

(10, 'Email Template Library', 'Centralize email templates.', 'Folder structure, naming conventions and component library.'),
(10, 'A/B Testing Framework', 'Framework for experiments.', 'Standard process for hypotheses, variants and analysis.'),

(11, 'Security Hardening', 'Security improvements project.', 'Checklist of encryption, password policies and monitoring.'),
(11, 'Access Logs Review', 'Analyze access logs.', 'Queries, dashboards and recurring review procedure.'),

(12, 'Infrastructure as Code', 'Automate infra with IaC.', 'Modules, environments and rollout plan for IaC adoption.'),
(12, 'Backup and Recovery Plan', 'Define backup policies.', 'RPO/RTO targets, schedules and recovery runbooks.'),

(13, 'Customer Journey Map', 'Map end-to-end customer journey.', 'Stages, touchpoints and responsibilities for each area.'),
(13, 'NPS Program', 'Implement NPS surveys.', 'Survey cadence, target segments and follow-up workflows.'),

(14, 'API v2 Design', 'Design of public API v2.', 'Endpoints, versioning strategy and deprecation policy.'),
(14, 'API Rate Limiting', 'Introduce rate limiting.', 'Limit definitions, error responses and configuration patterns.'),

(15, 'Partner Portal', 'Portal for partners.', 'Access model, enablement materials and reporting views.'),
(15, 'Partner Onboarding', 'Onboard new partners.', 'Checklist and automated communications for new partners.'),

(16, 'Content Calendar', 'Editorial calendar for blog.', 'Monthly themes, channels and responsible editors.'),
(16, 'Brand Guidelines', 'Brand and design guide.', 'Logo usage, typography, colors and tone of voice.'),

(17, 'OKR Definition', 'Define company OKRs.', 'Objectives, key results and tracking method.'),
(17, 'OKR Tracking Tool', 'Tool to monitor OKRs.', 'Views for teams, progress indicators and reminders.'),

(18, 'Performance Review Cycle', 'Annual performance reviews.', 'Timeline, forms and calibration sessions description.'),
(18, 'Training Catalog', 'Internal training catalog.', 'List of courses, skills and enrollment rules.'),

(19, 'Analytics Tracking Plan', 'Define tracking events.', 'Event list, properties and implementation notes.'),
(19, 'Data Governance Policy', 'Data governance project.', 'Roles, responsibilities and data lifecycle rules.'),

(20, 'Public Website Revamp', 'Revamp of corporate site.', 'New sitemap, layouts and migration from old CMS.'),
(20, 'Landing Page Factory', 'System for quick landings.', 'Templates, components and publishing workflow.'),

(21, 'Finance Dashboard', 'Financial metrics dashboard.', 'Revenue, burn rate, forecasts and variance analysis.'),
(21, 'Expense Policy Update', 'Update expense policies.', 'Rules, approval flow and communication plan.'),

(22, 'Internal Chat Migration', 'Migrate chat tool.', 'Requirements, migration steps and training sessions.'),
(22, 'Meeting Room Booking', 'Booking system for rooms.', 'Rules, integration with calendar and UI mockups.'),

(23, 'Incident Management', 'Define incident process.', 'Severities, SLA targets and communication templates.'),
(23, 'Postmortem Template', 'Template for incidents.', 'Sections, owners and action item tracking.'),

(24, 'Release Management', 'Release cycle definition.', 'Environments, change windows and rollback strategy.'),
(24, 'Feature Flag System', 'Feature toggling.', 'Flag taxonomy, tech stack and governance rules.'),

(25, 'Localization Project', 'Localize product to new languages.', 'Locales, translation workflow and QA checks.'),
(25, 'Accessibility Improvements', 'Improve accessibility.', 'Audit results and prioritized remediation actions.'),

(1, 'Sandbox Project A', 'Generic sandbox project.', 'Long generic content for testing pagination and queries.'),
(2, 'Sandbox Project B', 'Another sandbox project.', 'Another long body of text simulating realistic content.'),
(3, 'Sandbox Project C', 'Extra sandbox data.', 'Useful to stress-test lists, filters and permissions.'),
(4, 'Sandbox Project D', 'Load testing data.', 'Project created only to increase dataset size.'),
(5, 'Sandbox Project E', 'Seed data example.', 'Helps developers and QA when initializing databases.');