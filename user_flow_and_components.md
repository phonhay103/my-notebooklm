# User Flow and Component Hierarchy

## User Flows

### 1. Onboarding

1.  User visits the website.
2.  User is prompted to log in or sign up.
3.  User signs up or logs in.
4.  User is redirected to the main application view.

### 2. Create Notebook

1.  User clicks the "New Notebook" button.
2.  A new notebook is created with a default title.
3.  The user can then rename the notebook.

### 3. Add Source

1.  User selects a notebook.
2.  User clicks the "Add Source" button.
3.  User is presented with options to add a source (PDF, URL, etc.).
4.  User selects a source type and provides the source.
5.  The source is added to the notebook and processing begins.

### 4. Ask a Question

1.  User selects a notebook.
2.  User types a question in the chat input.
3.  User submits the question.
4.  The application displays the question in the chat window.
5.  The application displays a loading indicator while the answer is being generated.
6.  The application displays the answer in the chat window with citations.

## Component Hierarchy

*   **App** (Template)
    *   **MainLayout** (Template)
        *   **SourcesPanel** (Organism)
            *   **Button** (Atom)
            *   **SearchBar** (Molecule)
                *   **Input** (Atom)
                *   **Icon** (Atom)
            *   **SourceItem** (Molecule)
                *   **Icon** (Atom)
                *   **Text** (Atom)
                *   **Checkbox** (Atom)
        *   **ChatWindow** (Organism)
            *   **ChatBubble** (Molecule)
                *   **Avatar** (Atom)
                *   **Text** (Atom)
                *   **CitationLink** (Atom)
            *   **Input** (Atom)
        *   **StudioPanel** (Organism)
            *   **Button** (Atom)
            *   **AudioPlayer** (Molecule)
