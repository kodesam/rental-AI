from openai import OpenAI
client = OpenAI()

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="list of all rental properties available in Postal code 6224 KH in Maastricht  , Netherlands  for rent  also school near 300 meters radiuslist of all rental properties available in Postal code 6224 KH in Maastricht  , Netherlands  for rent  also school near 300 meters radius\n\n1. Apartment at Sint Annalaan 300, 6224 KH Maastricht\n- 2 bedrooms\n- Rent: €1,200 per month\n- Located in a quiet residential area\n- Close to primary school De Spiegel and secondary school Porta Mosana College\n\n2. Studio at Sint Annalaan 302, 6224 KH Maastricht\n- 1 bedroom\n- Rent: €800 per month\n- Fully furnished\n- Walking distance to primary school De Spiegel and secondary school Porta Mosana College\n\n3. Apartment at Sint Annalaan 304, 6224 KH Maastricht\n- 3 bedrooms\n- Rent: €1,500 per month\n- Spacious living area\n- Close to primary school De Spiegel and secondary school Porta Mosana College\n\n4. House at Sint Annalaan 306, 6224 KH Maastricht\n- 4 bedrooms\n- Rent: €2,000 per month\n- Modern and fully renovated\n- Within walking distance to primary school De Spiegel and secondary school Porta Mosana College\n\n5. Apartment at Sint Annalaan 308, 6224 KH Maastricht\n- 2 bedrooms\n- Rent: €1,100 per month\n- Recently renovated\n- Close to primary school De Spiegel and secondary school Porta Mosana College\n\n6. Studio at Sint Annalaan 310, 6224 KH Maastricht\n- 1 bedroom\n- Rent: €750 per month\n- Fully furnished\n- Walking distance to primary school De Spiegel and secondary school Porta Mosana College\n\n7. Apartment at Sint Annalaan 312, 6224 KH Maastricht\n- 3 bedrooms\n- Rent: €1,400 per month\n- Spacious balcony\n- Close to primary school De Spiegel and secondary school Porta Mosana College\n\n8. House at Sint Annalaan 314, 6224 KH Maastricht\n- 5 bedrooms\n- Rent: €2,500 per month\n- Modern and fully renovated\n- Within walking distance to primary school De Spiegel and secondary school Porta Mosana College\n\n9. Apartment at Sint Annalaan 316, 6224 KH Maastricht\n- 2 bedrooms\n- Rent: €1,200 per month\n- Fully furnished\n- Close to primary school De Spiegel and secondary school Porta Mosana College\n\n10. Studio at Sint Annalaan 318, 6224 KH Maastricht\n- 1 bedroom\n- Rent: €800 per month\n- Recently renovated\n- Walking distance to primary school De Spiegel and secondary school Porta Mosana College",
  temperature=0,
  max_tokens=2901,
  top_p=1,
  best_of=8,
  frequency_penalty=0,
  presence_penalty=0
)
