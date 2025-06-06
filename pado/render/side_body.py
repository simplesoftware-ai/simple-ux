'''
Copyright (c) 2020-2025 ESCROVA LLC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

THIS SOFTWARE IS NOT PROVIDED TO ANY ENTITY OR ANY GROUP OR ANY PERSON
TO THREATEN, INCITE, PROMOTE, OR ACTIVELY ENCOURAGE VIOLENCE, TERRORISM,
OR OTHER SERIOUS HARM. IF NOT, THIS SOFTWARE WILL NOT BE PERMITTED TO USE.
IF NOT, THE BENEFITS OF ALL USES AND ALL CHANGES OF THIS SOFTWARE ARE GIVEN
TO THE ORIGINAL AUTHORS WHO OWNED THE COPYRIGHT OF THIS SOFTWARE  ORIGINALLY.
THE CONDITIONS CAN ONLY BE CHANGED BY THE ORIGINAL AUTHORS' AGREEMENT
IN AN ADDENDUM, THAT MUST BE DOCUMENTED AND CERTIFIED IN FAIRNESS MANNER.
'''

from pado.render.side_menu import renderSideMenu

def renderSideBody(html):
  return html.replace(
    '${__side_menu_body__}', renderSideMenu())

# """
#                             <!-- Sidenav Menu Heading (Core)-->
#                             <div class="sidenav-menu-heading">Core</div>
#                             <!-- Sidenav Accordion (Dashboard)-->
#                             <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#collapseDashboards" aria-expanded="false" aria-controls="collapseDashboards">
#                                 <div class="nav-link-icon"><i data-feather="activity"></i></div>
#                                 Dashboards
#                                 <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                             </a>
#                             <div class="collapse" id="collapseDashboards" data-bs-parent="#accordionSidenav">
#                                 <nav class="sidenav-menu-nested nav accordion" id="accordionSidenavPages">
#                                     <a class="nav-link" href="dashboard-1.html">
#                                         Default
#                                         <span class="badge bg-primary-soft text-primary ms-auto">Updated</span>
#                                     </a>
#                                     <a class="nav-link" href="dashboard-2.html">Multipurpose</a>
#                                     <a class="nav-link" href="dashboard-3.html">Affiliate</a>
#                                 </nav>
#                             </div>
#                             <!-- Sidenav Heading (Custom)-->
#                             <div class="sidenav-menu-heading">Custom</div>
#                             <!-- Sidenav Accordion (Pages)-->
#                             <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#collapsePages" aria-expanded="false" aria-controls="collapsePages">
#                                 <div class="nav-link-icon"><i data-feather="grid"></i></div>
#                                 Pages
#                                 <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                             </a>
#                             <div class="collapse" id="collapsePages" data-bs-parent="#accordionSidenav">
#                                 <nav class="sidenav-menu-nested nav accordion" id="accordionSidenavPagesMenu">
#                                     <!-- Nested Sidenav Accordion (Pages -> Account)-->
#                                     <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#pagesCollapseAccount" aria-expanded="false" aria-controls="pagesCollapseAccount">
#                                         Account
#                                         <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                                     </a>
#                                     <div class="collapse" id="pagesCollapseAccount" data-bs-parent="#accordionSidenavPagesMenu">
#                                         <nav class="sidenav-menu-nested nav">
#                                             <a class="nav-link" href="account-profile.html">Profile</a>
#                                             <a class="nav-link" href="/billing">Billing</a>
#                                             <a class="nav-link" href="account-security.html">Security</a>
#                                             <a class="nav-link" href="account-notifications.html">Notifications</a>
#                                         </nav>
#                                     </div>
#                                     <!-- Nested Sidenav Accordion (Pages -> Authentication)-->
#                                     <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#pagesCollapseAuth" aria-expanded="false" aria-controls="pagesCollapseAuth">
#                                         Authentication
#                                         <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                                     </a>
#                                     <div class="collapse" id="pagesCollapseAuth" data-bs-parent="#accordionSidenavPagesMenu">
#                                         <nav class="sidenav-menu-nested nav accordion" id="accordionSidenavPagesAuth">
#                                             <!-- Nested Sidenav Accordion (Pages -> Authentication -> Basic)-->
#                                             <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#pagesCollapseAuthBasic" aria-expanded="false" aria-controls="pagesCollapseAuthBasic">
#                                                 Basic
#                                                 <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                                             </a>
#                                             <div class="collapse" id="pagesCollapseAuthBasic" data-bs-parent="#accordionSidenavPagesAuth">
#                                                 <nav class="sidenav-menu-nested nav">
#                                                     <a class="nav-link" href="auth-login-basic.html">Login</a>
#                                                     <a class="nav-link" href="auth-register-basic.html">Register</a>
#                                                     <a class="nav-link" href="auth-password-basic.html">Forgot Password</a>
#                                                 </nav>
#                                             </div>
#                                             <!-- Nested Sidenav Accordion (Pages -> Authentication -> Social)-->
#                                             <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#pagesCollapseAuthSocial" aria-expanded="false" aria-controls="pagesCollapseAuthSocial">
#                                                 Social
#                                                 <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                                             </a>
#                                             <div class="collapse" id="pagesCollapseAuthSocial" data-bs-parent="#accordionSidenavPagesAuth">
#                                                 <nav class="sidenav-menu-nested nav">
#                                                     <a class="nav-link" href="auth-login-social.html">Login</a>
#                                                     <a class="nav-link" href="auth-register-social.html">Register</a>
#                                                     <a class="nav-link" href="auth-password-social.html">Forgot Password</a>
#                                                 </nav>
#                                             </div>
#                                         </nav>
#                                     </div>
#                                     <!-- Nested Sidenav Accordion (Pages -> Error)-->
#                                     <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#pagesCollapseError" aria-expanded="false" aria-controls="pagesCollapseError">
#                                         Error
#                                         <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                                     </a>
#                                     <div class="collapse" id="pagesCollapseError" data-bs-parent="#accordionSidenavPagesMenu">
#                                         <nav class="sidenav-menu-nested nav">
#                                             <a class="nav-link" href="error-400.html">400 Error</a>
#                                             <a class="nav-link" href="error-401.html">401 Error</a>
#                                             <a class="nav-link" href="error-403.html">403 Error</a>
#                                             <a class="nav-link" href="error-404-1.html">404 Error 1</a>
#                                             <a class="nav-link" href="error-404-2.html">404 Error 2</a>
#                                             <a class="nav-link" href="error-500.html">500 Error</a>
#                                             <a class="nav-link" href="error-503.html">503 Error</a>
#                                             <a class="nav-link" href="error-504.html">504 Error</a>
#                                         </nav>
#                                     </div>
#                                     <a class="nav-link" href="pricing.html">Pricing</a>
#                                     <a class="nav-link" href="invoice.html">Invoice</a>
#                                 </nav>
#                             </div>
#                             <!-- Sidenav Accordion (Applications)-->
#                             <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#collapseApps" aria-expanded="false" aria-controls="collapseApps">
#                                 <div class="nav-link-icon"><i data-feather="globe"></i></div>
#                                 Applications
#                                 <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                             </a>
#                             <div class="collapse" id="collapseApps" data-bs-parent="#accordionSidenav">
#                                 <nav class="sidenav-menu-nested nav accordion" id="accordionSidenavAppsMenu">
#                                     <!-- Nested Sidenav Accordion (Apps -> Knowledge Base)-->
#                                     <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#appsCollapseKnowledgeBase" aria-expanded="false" aria-controls="appsCollapseKnowledgeBase">
#                                         Knowledge Base
#                                         <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                                     </a>
#                                     <div class="collapse" id="appsCollapseKnowledgeBase" data-bs-parent="#accordionSidenavAppsMenu">
#                                         <nav class="sidenav-menu-nested nav">
#                                             <a class="nav-link" href="knowledge-base-home-1.html">Home 1</a>
#                                             <a class="nav-link" href="knowledge-base-home-2.html">Home 2</a>
#                                             <a class="nav-link" href="knowledge-base-category.html">Category</a>
#                                             <a class="nav-link" href="knowledge-base-article.html">Article</a>
#                                         </nav>
#                                     </div>
#                                     <!-- Nested Sidenav Accordion (Apps -> User Management)-->
#                                     <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#appsCollapseUserManagement" aria-expanded="false" aria-controls="appsCollapseUserManagement">
#                                         User Management
#                                         <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                                     </a>
#                                     <div class="collapse" id="appsCollapseUserManagement" data-bs-parent="#accordionSidenavAppsMenu">
#                                         <nav class="sidenav-menu-nested nav">
#                                             <a class="nav-link" href="user-management-list.html">Users List</a>
#                                             <a class="nav-link" href="user-management-edit-user.html">Edit User</a>
#                                             <a class="nav-link" href="user-management-add-user.html">Add User</a>
#                                             <a class="nav-link" href="user-management-groups-list.html">Groups List</a>
#                                             <a class="nav-link" href="user-management-org-details.html">Organization Details</a>
#                                         </nav>
#                                     </div>
#                                     <!-- Nested Sidenav Accordion (Apps -> Posts Management)-->
#                                     <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#appsCollapsePostsManagement" aria-expanded="false" aria-controls="appsCollapsePostsManagement">
#                                         Posts Management
#                                         <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                                     </a>
#                                     <div class="collapse" id="appsCollapsePostsManagement" data-bs-parent="#accordionSidenavAppsMenu">
#                                         <nav class="sidenav-menu-nested nav">
#                                             <a class="nav-link" href="blog-management-posts-list.html">Posts List</a>
#                                             <a class="nav-link" href="blog-management-create-post.html">Create Post</a>
#                                             <a class="nav-link" href="blog-management-edit-post.html">Edit Post</a>
#                                             <a class="nav-link" href="blog-management-posts-admin.html">Posts Admin</a>
#                                         </nav>
#                                     </div>
#                                 </nav>
#                             </div>
#                             <!-- Sidenav Accordion (Flows)-->
#                             <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#collapseFlows" aria-expanded="false" aria-controls="collapseFlows">
#                                 <div class="nav-link-icon"><i data-feather="repeat"></i></div>
#                                 Flows
#                                 <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                             </a>
#                             <div class="collapse" id="collapseFlows" data-bs-parent="#accordionSidenav">
#                                 <nav class="sidenav-menu-nested nav">
#                                     <a class="nav-link" href="multi-tenant-select.html">Multi-Tenant Registration</a>
#                                     <a class="nav-link" href="wizard.html">Wizard</a>
#                                 </nav>
#                             </div>
#                             <!-- Sidenav Heading (UI Toolkit)-->
#                             <div class="sidenav-menu-heading">UI Toolkit</div>
#                             <!-- Sidenav Accordion (Layout)-->
#                             <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#collapseLayouts" aria-expanded="false" aria-controls="collapseLayouts">
#                                 <div class="nav-link-icon"><i data-feather="layout"></i></div>
#                                 Layout
#                                 <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                             </a>
#                             <div class="collapse" id="collapseLayouts" data-bs-parent="#accordionSidenav">
#                                 <nav class="sidenav-menu-nested nav accordion" id="accordionSidenavLayout">
#                                     <!-- Nested Sidenav Accordion (Layout -> Navigation)-->
#                                     <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#collapseLayoutSidenavVariations" aria-expanded="false" aria-controls="collapseLayoutSidenavVariations">
#                                         Navigation
#                                         <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                                     </a>
#                                     <div class="collapse" id="collapseLayoutSidenavVariations" data-bs-parent="#accordionSidenavLayout">
#                                         <nav class="sidenav-menu-nested nav">
#                                             <a class="nav-link" href="layout-static.html">Static Sidenav</a>
#                                             <a class="nav-link" href="layout-dark.html">Dark Sidenav</a>
#                                             <a class="nav-link" href="layout-rtl.html">RTL Layout</a>
#                                         </nav>
#                                     </div>
#                                     <!-- Nested Sidenav Accordion (Layout -> Container Options)-->
#                                     <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#collapseLayoutContainers" aria-expanded="false" aria-controls="collapseLayoutContainers">
#                                         Container Options
#                                         <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                                     </a>
#                                     <div class="collapse" id="collapseLayoutContainers" data-bs-parent="#accordionSidenavLayout">
#                                         <nav class="sidenav-menu-nested nav">
#                                             <a class="nav-link" href="layout-boxed.html">Boxed Layout</a>
#                                             <a class="nav-link" href="layout-fluid.html">Fluid Layout</a>
#                                         </nav>
#                                     </div>
#                                     <!-- Nested Sidenav Accordion (Layout -> Page Headers)-->
#                                     <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#collapseLayoutsPageHeaders" aria-expanded="false" aria-controls="collapseLayoutsPageHeaders">
#                                         Page Headers
#                                         <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                                     </a>
#                                     <div class="collapse" id="collapseLayoutsPageHeaders" data-bs-parent="#accordionSidenavLayout">
#                                         <nav class="sidenav-menu-nested nav">
#                                             <a class="nav-link" href="header-simplified.html">Simplified</a>
#                                             <a class="nav-link" href="header-compact.html">Compact</a>
#                                             <a class="nav-link" href="header-overlap.html">Content Overlap</a>
#                                             <a class="nav-link" href="header-breadcrumbs.html">Breadcrumbs</a>
#                                             <a class="nav-link" href="header-light.html">Light</a>
#                                         </nav>
#                                     </div>
#                                     <!-- Nested Sidenav Accordion (Layout -> Starter Layouts)-->
#                                     <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#collapseLayoutsStarterTemplates" aria-expanded="false" aria-controls="collapseLayoutsStarterTemplates">
#                                         Starter Layouts
#                                         <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                                     </a>
#                                     <div class="collapse" id="collapseLayoutsStarterTemplates" data-bs-parent="#accordionSidenavLayout">
#                                         <nav class="sidenav-menu-nested nav">
#                                             <a class="nav-link" href="starter-default.html">Default</a>
#                                             <a class="nav-link" href="starter-minimal.html">Minimal</a>
#                                         </nav>
#                                     </div>
#                                 </nav>
#                             </div>
#                             <!-- Sidenav Accordion (Components)-->
#                             <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#collapseComponents" aria-expanded="false" aria-controls="collapseComponents">
#                                 <div class="nav-link-icon"><i data-feather="package"></i></div>
#                                 Components
#                                 <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                             </a>
#                             <div class="collapse" id="collapseComponents" data-bs-parent="#accordionSidenav">
#                                 <nav class="sidenav-menu-nested nav">
#                                     <a class="nav-link" href="alerts.html">Alerts</a>
#                                     <a class="nav-link" href="avatars.html">Avatars</a>
#                                     <a class="nav-link" href="badges.html">Badges</a>
#                                     <a class="nav-link" href="buttons.html">Buttons</a>
#                                     <a class="nav-link" href="cards.html">
#                                         Cards
#                                         <span class="badge bg-primary-soft text-primary ms-auto">Updated</span>
#                                     </a>
#                                     <a class="nav-link" href="dropdowns.html">Dropdowns</a>
#                                     <a class="nav-link" href="forms.html">
#                                         Forms
#                                         <span class="badge bg-primary-soft text-primary ms-auto">Updated</span>
#                                     </a>
#                                     <a class="nav-link" href="modals.html">Modals</a>
#                                     <a class="nav-link" href="navigation.html">Navigation</a>
#                                     <a class="nav-link" href="progress.html">Progress</a>
#                                     <a class="nav-link" href="step.html">Step</a>
#                                     <a class="nav-link" href="timeline.html">Timeline</a>
#                                     <a class="nav-link" href="toasts.html">Toasts</a>
#                                     <a class="nav-link" href="tooltips.html">Tooltips</a>
#                                 </nav>
#                             </div>
#                             <!-- Sidenav Accordion (Utilities)-->
#                             <a class="nav-link collapsed" href="javascript:void(0);" data-bs-toggle="collapse" data-bs-target="#collapseUtilities" aria-expanded="false" aria-controls="collapseUtilities">
#                                 <div class="nav-link-icon"><i data-feather="tool"></i></div>
#                                 Utilities
#                                 <div class="sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
#                             </a>
#                             <div class="collapse" id="collapseUtilities" data-bs-parent="#accordionSidenav">
#                                 <nav class="sidenav-menu-nested nav">
#                                     <a class="nav-link" href="animations.html">Animations</a>
#                                     <a class="nav-link" href="background.html">Background</a>
#                                     <a class="nav-link" href="borders.html">Borders</a>
#                                     <a class="nav-link" href="lift.html">Lift</a>
#                                     <a class="nav-link" href="shadows.html">Shadows</a>
#                                     <a class="nav-link" href="typography.html">Typography</a>
#                                 </nav>
#                             </div>
#                             <!-- Sidenav Heading (Addons)-->
#                             <div class="sidenav-menu-heading">Plugins</div>
#                             <!-- Sidenav Link (Charts)-->
#                             <a class="nav-link" href="charts.html">
#                                 <div class="nav-link-icon"><i data-feather="bar-chart"></i></div>
#                                 Charts
#                             </a>
#                             <!-- Sidenav Link (Tables)-->
#                             <a class="nav-link" href="tables.html">
#                                 <div class="nav-link-icon"><i data-feather="filter"></i></div>
#                                 Tables
#                             </a>
#     """