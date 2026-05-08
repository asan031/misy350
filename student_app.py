"""
Phase 2 Student-Facing Streamlit App.

This app uses the refactored backend from Session 1:
- EnrollmentDatabase handles database/SQL work.
- EnrollmentService handles enrollment rules.
- The Streamlit UI calls the service layer instead of writing SQL directly.

Run with:
    streamlit run student_app.py
"""

from __future__ import annotations

import streamlit as st

from enrollment_refactored import (
    CURRENT_STUDENT,
    EnrollmentDatabase,
    EnrollmentService,
)


# ------------------------------------------------------------
# Backend setup
# ------------------------------------------------------------

@st.cache_resource
def get_service() -> EnrollmentService:
    """Create and return the enrollment service."""
    database = EnrollmentDatabase()
    database.create_tables()
    database.seed_sample_data()
    return EnrollmentService(database)


service = get_service()


# ------------------------------------------------------------
# Session state setup
# ------------------------------------------------------------

def initialize_session_state() -> None:
    """Set default session state values for the student app."""
    if "page" not in st.session_state:
        st.session_state["page"] = "dashboard"

    if "selected_class" not in st.session_state:
        st.session_state["selected_class"] = None

    if "role" not in st.session_state:
        st.session_state["role"] = "student"

    if "current_student" not in st.session_state:
        st.session_state["current_student"] = CURRENT_STUDENT

    if "feedback_message" not in st.session_state:
        st.session_state["feedback_message"] = ""

    if "feedback_type" not in st.session_state:
        st.session_state["feedback_type"] = ""


def show_feedback() -> None:
    """Show a success, warning, or error message from session state."""
    message = st.session_state.get("feedback_message", "")
    feedback_type = st.session_state.get("feedback_type", "")

    if not message:
        return

    if feedback_type == "success":
        st.success(message)
    elif feedback_type == "warning":
        st.warning(message)
    elif feedback_type == "error":
        st.error(message)
    else:
        st.info(message)


def set_feedback(message: str, feedback_type: str) -> None:
    """Store a feedback message in session state."""
    st.session_state["feedback_message"] = message
    st.session_state["feedback_type"] = feedback_type


def clear_feedback() -> None:
    """Clear the current feedback message."""
    st.session_state["feedback_message"] = ""
    st.session_state["feedback_type"] = ""


def require_student_role() -> bool:
    """Check that the simulated role is student."""
    if st.session_state.get("role") != "student":
        st.error("You must have the student role to access this dashboard.")
        return False

    return True


# ------------------------------------------------------------
# Page helpers
# ------------------------------------------------------------

def go_to_class(selected_class: dict) -> None:
    """Store a selected class and move to the class detail page."""
    st.session_state["selected_class"] = selected_class
    st.session_state["page"] = "class_detail"


def back_to_dashboard() -> None:
    """Return to the dashboard page."""
    st.session_state["page"] = "dashboard"
    st.session_state["selected_class"] = None
    clear_feedback()


# ------------------------------------------------------------
# Page 1: Student Dashboard
# ------------------------------------------------------------

def render_dashboard() -> None:
    """Render the student dashboard page."""
    student = st.session_state["current_student"]
    user_id = student["user_id"]
    email = student["email"]

    st.title("Student Class Dashboard")
    st.caption(
        f"Logged in as {student['name']} | {student['email']} | "
        f"Role: {st.session_state['role']}"
    )

    show_feedback()

    st.divider()

    with st.container():
        st.subheader("Enroll in a Class")

        with st.form("enrollment_form"):
            enrollment_key = st.text_input(
                "Enter enrollment key",
                placeholder="Example: DATA210-SPRING",
            )
            submitted = st.form_submit_button("Submit Enrollment Key")

        if submitted:
            enrolled_class = service.enroll_with_key(
                user_id=user_id,
                email=email,
                enrollment_key=enrollment_key,
            )

            if enrolled_class:
                set_feedback(
                    f"Enrollment successful for {enrolled_class['course_id']}.",
                    "success",
                )
                st.session_state["selected_class"] = enrolled_class
                st.session_state["page"] = "class_detail"
                st.rerun()
            else:
                set_feedback(
                    "That enrollment key is missing or invalid. Please try again.",
                    "error",
                )
                st.rerun()

    st.divider()

    with st.container():
        st.subheader("My Enrolled Classes")

        enrolled_classes = service.get_student_enrollments(user_id)

        if not enrolled_classes:
            st.warning("You are not currently enrolled in any classes.")
            return

        st.dataframe(enrolled_classes, use_container_width=True)

        st.divider()

        for course in enrolled_classes:
            with st.container():
                st.markdown(f"**{course['course_id']}: {course['course_name']}**")
                st.caption(
                    f"Instructor: {course['instructor']} | "
                    f"Status: {course['status']} | "
                    f"Enrolled: {course.get('enrolled_at', 'N/A')}"
                )

                go_col, unenroll_col = st.columns(2)

                with go_col:
                    if st.button(
                        "Go to Class",
                        key=f"go_{course['course_id']}",
                    ):
                        clear_feedback()
                        go_to_class(course)
                        st.rerun()

                with unenroll_col:
                    if st.button(
                        "Unenroll",
                        key=f"unenroll_{course['course_id']}",
                    ):
                        success = service.soft_unenroll_student(
                            user_id=user_id,
                            course_id=course["course_id"],
                        )

                        if success:
                            set_feedback(
                                f"You have been unenrolled from {course['course_id']}.",
                                "warning",
                            )
                        else:
                            set_feedback(
                                "Unable to unenroll from that class.",
                                "error",
                            )

                        st.rerun()

                st.divider()


# ------------------------------------------------------------
# Page 2: Selected Class Page
# ------------------------------------------------------------

def render_class_detail() -> None:
    """Render the selected class detail page."""
    student = st.session_state["current_student"]
    selected_class = st.session_state.get("selected_class")

    st.title("Selected Class")
    st.caption(f"Student: {student['name']} | {student['email']}")

    show_feedback()

    st.divider()

    if not selected_class:
        st.warning("No class is currently selected.")
        if st.button("Back to Dashboard"):
            back_to_dashboard()
            st.rerun()
        return

    with st.container():
        st.subheader(selected_class.get("course_name", "Class Details"))

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Course ID", selected_class.get("course_id", "N/A"))
            st.metric("Status", selected_class.get("status", "N/A"))

        with col2:
            st.metric("Instructor", selected_class.get("instructor", "N/A"))
            st.metric("Enrolled At", selected_class.get("enrolled_at", "N/A"))

        st.divider()

        st.write(f"**Course Name:** {selected_class.get('course_name', 'N/A')}")
        st.write(f"**Student Email:** {student['email']}")

    st.divider()

    if st.button("Back to Dashboard"):
        back_to_dashboard()
        st.rerun()


# ------------------------------------------------------------
# App Router
# ------------------------------------------------------------

def main() -> None:
    """Run the Streamlit app."""
    st.set_page_config(
        page_title="Student Enrollment App",
        page_icon="🎓",
        layout="wide",
    )

    initialize_session_state()

    if not require_student_role():
        st.stop()

    if st.session_state["page"] == "dashboard":
        render_dashboard()
    elif st.session_state["page"] == "class_detail":
        render_class_detail()
    else:
        st.session_state["page"] = "dashboard"
        render_dashboard()


if __name__ == "__main__":
    main()
