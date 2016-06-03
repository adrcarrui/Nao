package minimal;

import java.io.IOException;
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.*;
import java.net.*;

import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.ServletHandler;

import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONException;
import org.json.JSONTokener;
import org.json.HTTP;
 

import java.text.ParseException;


public class MinimalServlets
	
{	

    public static void main( String[] args ) throws Exception
    {   
        

        
        Server server = new Server(9000);


        ServletHandler handler = new ServletHandler();
        server.setHandler(handler);

	handler.addServletWithMapping(HelloServlet.class, "/*");
	
        server.start();
	server.join();

	
	
    }


    @SuppressWarnings("serial")
    public static class HelloServlet extends HttpServlet
    {

	
        @Override
        protected void doGet( HttpServletRequest request,
                              HttpServletResponse response ) throws ServletException,
                                                            IOException
        {
            response.setContentType("text/html");
            response.setStatus(HttpServletResponse.SC_OK);
            response.getWriter().println("<h1>Hello from HelloServlet</h1>");
	
        }

 	@Override
    	protected void doPost(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException 
	{
	PrintWriter out = resp.getWriter();
	BufferedReader br = new BufferedReader(new InputStreamReader(req.getInputStream()));
        	String json = "";
		if(br != null){
            		json = br.readLine();
 		//out.print(json);
		}
		System.out.println(json);
		JSONObject jsonObject;
		jsonObject = new JSONObject(json);
		String id = jsonObject.getString("identificador");
		//String edad = jsonObject.getString("edad");
		/*JSONArray jarray;
		jarray = jsonObject.getJSONArray("productos");
		JSONObject nuevasf;
		String[] aux = new String[nfrases];*/	
	
		//try{
    	//JSONObject jsonObject = org.json.HTTP.toJSONObject(json);
	//jsonObject = new JSONObject(json);
		//out.print("-->"+jsonObject.get("identificador"));
	
		//} catch (JSONException e) {
		//throw new IOException("Prueba 1 Error parsing JSON request string");*/
	
	//MinimalServlets.enviaMensaje(jsonObject.getString("name"));
	// {nFrases:2,productos:[{frase:"Bienvenido"},{frase:"Hola"}]}
	
		/*for (int n=0;n<nfrases;n++)
		{
			nuevasf = (JSONObject)jarray.get(n);
			aux[n] = nuevasf.getString("frase");		
			
		}*/

	//DataInputStream in;
      	//PrintWriter out = resp.getWriter();
	//BufferedReader rd = new BufferedReader(new InputStreamReader(in.getInputStream()));
	System.out.println(req);
	System.out.println(resp);
	System.out.println(id);
	System.out.println("\n");
	//BufferedReader wr = new BufferedReader(new InputStreamReader(conn.getOutputStream()));
	/*String clientIP = req.getRemoteAddr();
	String clientHOST = req.getRemoteHost();
        resp.setContentType("text/plain");
        PrintWriter out = resp.getWriter();
        out.println("IP  : " + clientIP);
        out.println("Host: " + clientHost);*/ 
        }
 	  
    
	
   }    
}
