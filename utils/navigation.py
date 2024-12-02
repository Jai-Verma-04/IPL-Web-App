import streamlit as st
from streamlit_option_menu import option_menu

pages_list = ["Home", "IPL Summary", "Head to Head Stats", "Generate Scorecard", 
              "Player Wise Stats", "Season Wise Stats", "Team Wise Stats", "Venue Wise Stats"]

pages_icons = ["house-fill", "bar-chart-fill", "bi-trophy-fill", "123", "person-fill", "calendar-fill", "people-fill", "bi-geo-alt-fill"]
def custom_sidebar_navigation(current_page):
#     st.markdown(
#     """
#     <style>
#         /* Hide default sidebar */
#         [data-testid="stSidebarNav"] {
#             display: none;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

        
    # Sidebar content
    with st.sidebar:
        with st.expander("Navigation"):
            selected_page = option_menu(
                "",    
                pages_list,
                default_index=pages_list.index(current_page),
                orientation='v',
                icons = pages_icons,
            )

    # Switch page if the selected page is different
    if selected_page != current_page:
        if selected_page != "Home":
            st.switch_page(f"pages\\{selected_page}.py")
        elif selected_page == "Home":
            st.switch_page("HOME.py")
