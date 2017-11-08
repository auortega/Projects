
import org.semanticweb.owlapi.model.OWLOntologyCreationException;
import org.semanticweb.owlapi.model.OWLOntologyStorageException;
import org.semanticweb.owlapi.util.DefaultPrefixManager;
import org.semanticweb.owlapi.model.*;
import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.model.OWLOntology;
import org.semanticweb.owlapi.model.OWLDataFactory;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;



public class MyOntology {
	
	String ontFile;
	static OWLOntologyManager manager;
	static OWLDataFactory factory;
	static File saveFile;
	static File file;
	static OWLOntology myOntology;
	static PrefixManager pm;
	
	public static void initializePopulation() throws OWLOntologyCreationException{
		String ontFile = "SMOntologyTest.owl";
		String sourceFile = "Smart_Mobility_Assignment_2_Blank.owl";
		//Managers First
		//Factory
		manager = OWLManager.createOWLOntologyManager();
		factory = manager.getOWLDataFactory();
		
		saveFile = new File("\\C:\\Users\\auort\\Documents\\"+ ontFile);
		file = new File ("\\C:\\Users\\auort\\Documents\\"+ sourceFile);
		
		myOntology = manager.loadOntologyFromOntologyDocument(file);
		
		//The issue with the population structure lies within the PrefixManager.
		pm = new DefaultPrefixManager("http://www.semanticweb.org/auort/ontologies/2017/3/untitled-ontology-15/");
	}
	
	public static void setIndividual(String individualName, OWLClass ontologyClass){
		OWLNamedIndividual individual = factory.getOWLNamedIndividual(individualName, pm);
		OWLClassAssertionAxiom classAssertion = factory.getOWLClassAssertionAxiom(ontologyClass, individual);
		manager.applyChange(new AddAxiom(myOntology, classAssertion));
	}
	
	public static void setIntData(OWLDataProperty property, String individualName, int value){
		OWLNamedIndividual individual = factory.getOWLNamedIndividual(individualName, pm);
		OWLAxiom axiom = factory.getOWLDataPropertyAssertionAxiom(property, individual, value);
		manager.applyChange(new AddAxiom(myOntology, axiom));
	}
	
	public static void setBoolData(OWLDataProperty property, String individualName, Boolean value){
		OWLNamedIndividual individual = factory.getOWLNamedIndividual(individualName, pm);
		OWLAxiom axiom = factory.getOWLDataPropertyAssertionAxiom(property, individual, value);
		manager.applyChange(new AddAxiom(myOntology, axiom));
	}
	
	public static void setStringData(OWLDataProperty property, String individualName, String value){
		OWLNamedIndividual individual = factory.getOWLNamedIndividual(individualName, pm);
		OWLAxiom axiom = factory.getOWLDataPropertyAssertionAxiom(property, individual, value);
		manager.applyChange(new AddAxiom(myOntology, axiom));
	}
	
	public static void saveOntology(){
		try{
			saveFile.createNewFile();
			FileOutputStream outputStream = new FileOutputStream(saveFile);
			manager.saveOntology(myOntology, outputStream);
			System.out.println("No exceptions thrown!");
		}catch(IOException e){
		}catch(OWLOntologyStorageException e){	
		}
		System.out.println("Save File: "+ saveFile);
		System.out.println();
	}
}
