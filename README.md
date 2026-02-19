# VectorShift-Pipeline-Builder-
This project is a visual pipeline builder built using React and FastAPI. Users can create workflows by connecting nodes and validate whether the pipeline forms a Directed Acyclic Graph (DAG).


Features:

- Reusable Node Abstraction (BaseNode architecture)
- Dynamic Text Node with auto-resize
- Variable detection using {{variable}} syntax
- Backend DAG validation
- Node & Edge counting
- Clean UI with unified styling

Tech Stack
Frontend:
- React
- React Flow
- CSS / Tailwind (if used)

Backend:
- Python
- FastAPI
- Uvicorn


 How To Run
      Frontend:
       cd frontend
        npm install
          npm start

       Backend:
     cd backend
    uvicorn main:app --reload




  
