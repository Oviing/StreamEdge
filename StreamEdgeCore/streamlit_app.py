import streamlit as st
import sqlite3
import time
import os

def get_table_names(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    return tables

def get_table_data(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()
    return columns, rows

def config_page():
    st.title("Configuration")
    db_path = st.text_input("Database path", value=st.session_state.get("db_path", "data.db"))
    if st.button("Save DB Path"):
        st.session_state["db_path"] = db_path
        st.success(f"Database path set to: {db_path}")

def viewer_page():
    st.title("Database Viewer & Chart Creator")
    db_path = st.session_state.get("db_path", "data.db")
    if not os.path.exists(db_path):
        st.error(f"Database file not found: {db_path}")
        return
    refresh_interval = st.sidebar.slider("Auto-refresh interval (seconds)", 2, 30, 5)
    last_refresh = st.session_state.get("last_refresh", time.time())
    if time.time() - last_refresh > refresh_interval:
        st.session_state["last_refresh"] = time.time()
        st.experimental_rerun()
    conn = sqlite3.connect(db_path)
    tables = get_table_names(conn)
    if not tables:
        st.write("No tables found in the database.")
        conn.close()
        return
    table = st.selectbox("Select a table to view:", tables)
    columns, rows = get_table_data(conn, table)
    st.write(f"Showing data for table: {table}")
    data = [dict(zip(columns, row)) for row in rows]
    st.dataframe(data)

    if data:
        st.subheader("Create a Chart")
        numeric_columns = [col for col in columns if isinstance(data[0][col], (int, float))]
        if len(numeric_columns) >= 1:
            x_col = st.selectbox("X axis:", columns)
            y_col = st.selectbox("Y axis:", numeric_columns)
            chart_type = st.selectbox("Chart type:", ["Line", "Bar", "Area"])
            import pandas as pd
            df = pd.DataFrame(data)
            if chart_type == "Line":
                st.line_chart(df[[x_col, y_col]].set_index(x_col))
            elif chart_type == "Bar":
                st.bar_chart(df[[x_col, y_col]].set_index(x_col))
            elif chart_type == "Area":
                st.area_chart(df[[x_col, y_col]].set_index(x_col))
        else:
            st.write("No numeric columns available for charting.")
    conn.close()

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Viewer", "Configuration"])
    if page == "Configuration":
        config_page()
    else:
        viewer_page()

if __name__ == "__main__":
    main()
