package minimal;

import java.io.IOException;
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.*;
import java.net.*;
import java.net.HttpURLConnection;
import java.net.URL;
import org.eclipse.jetty.util.Fields;
import org.eclipse.jetty.util.Fields.Field;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.net.ssl.HttpsURLConnection;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.ServletHandler;
import org.eclipse.jetty.client.HttpClient;
import org.eclipse.jetty.client.HttpExchange;
import org.eclipse.jetty.client.api.ContentResponse;

import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONException;
import org.json.JSONTokener;
import org.json.HTTP;
 

import java.text.ParseException;


public class MinimalServlets
	
{	static boolean info_nao_enviar;
	public static void sendPost(String cadena) throws Exception
	{
	try
	{	
		//PrintWriter out = resp.getWriter();
		JSONObject object = new JSONObject();
		object.put("identificador", cadena);	
		//System.out.println(object);
    	// Send data
    		URL url = new URL("http://localhost:9000");
    		URLConnection conn = url.openConnection();
    		conn.setDoOutput(true);
    		OutputStreamWriter wr = new OutputStreamWriter(conn.getOutputStream());
		wr.write(object.toString());    	
    		wr.flush();

    	// Get the response
    		BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
		System.out.println(rd);   		
		String line;
    			while ((line = rd.readLine()) != null) {
        // Process line...
				
    			}	
		System.out.println(rd);
    		wr.close();
    		rd.close();
		
		System.out.println(info_nao_enviar);
		info_nao_enviar = false;
		System.out.println(object);
		//out.print(object);
	}		
	catch (Exception e) { 
		e.printStackTrace();}	
	

	}


	public static void enviaMensaje(String cadena)
	{
	try{
		Socket soc= new Socket("localhost", 9999);
        	DataOutputStream dout= new DataOutputStream(soc.getOutputStream());
		dout.writeUTF(cadena);
		System.out.println(cadena);
		System.out.println(info_nao_enviar);
		info_nao_enviar = false;
		System.out.println(info_nao_enviar);
        	dout.flush();
        	dout.close();
        	soc.close();
	}
	catch(Exception e){
                e.printStackTrace();}
	}
	
	public static void escuchaYenvia()
	{
	try
	{	
		ServerSocket soc2 = new ServerSocket(9998);		
		Socket MiServicio = soc2.accept();
		System.out.println("Estableciendo conexion...");
		System.out.println(MiServicio);
        	BufferedReader entrada = new BufferedReader(new InputStreamReader(MiServicio.getInputStream()));
		String mensajeRecibido = entrada.readLine();		
		entrada.close();
		int longitud = mensajeRecibido.length();
		//System.out.println(longitud);
		String id = mensajeRecibido.substring(0,3);		
		String recorte = mensajeRecibido.substring(longitud-3,longitud);
		String informacion = mensajeRecibido.substring(id.length(), longitud - recorte.length() - 1);
		//String norecorte = mensajeRecibido.substring(0,longitud-3);
		System.out.println(info_nao_enviar);
		System.out.println(id);
		System.out.println(informacion);
		System.out.println(recorte);
		if(recorte.equals("FIN"))
		{
				
		soc2.close();
		info_nao_enviar = true;
		MinimalServlets.sendPost(informacion);
		}
		
		//soc2.close();
	}
	catch(Exception e){
                e.printStackTrace();}
	}
	

    public static void main( String[] args ) throws Exception
    {   
        

        //El servidor escucha en el puerto 8081
        Server server = new Server(8081);


        ServletHandler handler = new ServletHandler();
        server.setHandler(handler);

	handler.addServletWithMapping(HelloServlet.class, "/*");
	info_nao_enviar = false;
        server.start();
	//server.join();
	while(true)
	{	
	MinimalServlets.escuchaYenvia();
	}
	
	//server.join();

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
       	if(info_nao_enviar == false)
	{
	//SACAR CAMPOS DE JSON
        	BufferedReader br = new BufferedReader(new InputStreamReader(req.getInputStream()));
        	String json = "";
		if(br != null){
            		json = br.readLine();
 		out.print(json);}
		String DatosAPython = "";
		JSONObject jsonObject;
		jsonObject = new JSONObject(json);
		int nfrases = jsonObject.getInt("nFrases");
		JSONArray jarray;
		jarray = jsonObject.getJSONArray("productos");
		JSONObject nuevasf;
		String[] aux = new String[nfrases];	
	
		try{
    	//JSONObject jsonObject = org.json.HTTP.toJSONObject(json);
	//jsonObject = new JSONObject(json);
		out.print("-->"+jsonObject.get("nFrases"));
	
		} catch (JSONException e) {
		throw new IOException("Prueba 1 Error parsing JSON request string");
	}
	//MinimalServlets.enviaMensaje(jsonObject.getString("name"));
	// {nFrases:2,productos:[{frase:"Bienvenido"},{frase:"Hola"}]}
	
		for (int n=0;n<nfrases;n++)
		{
			nuevasf = (JSONObject)jarray.get(n);
			aux[n] = nuevasf.getString("frase");		
			DatosAPython = aux[n] + DatosAPython;
		}
	
	MinimalServlets.enviaMensaje(DatosAPython);
	info_nao_enviar = false;
	
	//MinimalServlets.escuchaYenvia();

	}
	
	if (info_nao_enviar == true)
	{
		//JSONObject object = new JSONObject();
		System.out.println("Entro en el POST"); 
	}       
		//try {
            //object.put("identificador", "Nao");
            //object.put("age", "26");
	    
	    //JSONObject object = new JSONObject("{\"identificador\":\"Nao\"}");//\"edad\":\"3000\"}");
//System.out.println("JSon enviado");
	    //System.out.println(object);
	    //out.print(object);
	   
   
        
    // Construct data
    	//StringBuilder dataBuilder = new StringBuilder();
    	//dataBuilder.append(URLEncoder.encode("key1", "UTF-8")).append('=').append(URLEncoder.encode("value1", "UTF-8")).
       	//append(URLEncoder.encode("key2", "UTF-8")).append('=').append(URLEncoder.encode("value2", "UTF-8"));
	
//FUNCIONA	
	/*String dataBuilder = "HelloWorld";	
	System.out.println(dataBuilder);
    // Send data
    	URL url = new URL("http://localhost:9000");
    	URLConnection conn = url.openConnection();
    	conn.setDoOutput(true);
    	OutputStreamWriter wr = new OutputStreamWriter(conn.getOutputStream());
	wr.write(object.toString());    	
	//wr.write(dataBuilder.toString());
    	wr.flush();

    // Get the response
    	BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
    	String line;
    	while ((line = rd.readLine()) != null) {
        // Process line...
    	}
	System.out.println(rd);
    	wr.close();
    	rd.close();
	
		
	System.out.println(info_nao_enviar);
	info_nao_enviar = false;
	//MinimalServlets.sendPost();
		}	
	catch (Exception e) { e.printStackTrace();}	
	}
	*/
	//Json a pegar en HTTP requester {"nFrases": "2","0":"Hola1","1":"Bienvenidos1","2":"Fin"}
//MinimalServlets.dout, jsonObject.getString("name"));
	/*JSONObject object = new JSONObject();
        try {
            object.put("name", jsonObject.get("name"));
            object.put("age", "26");
        } catch (Exception ex) {
            out.print("Error: " + ex.getMessage());
        }
     
	out.println(object.getString("name"));*/
	/*processRequest(req, resp);
	String datos = "";
	try{
	datos = "Hola, esto es una prueba con POST";
	out.println(datos);
	}
	catch(Exception e){
	e.printStackTrace();
	out.println("Error al recibir parámetros con POST");
	out.println(e);
	out.close();
	return;*/
	//}
	
        }
 	
    }
    
}
