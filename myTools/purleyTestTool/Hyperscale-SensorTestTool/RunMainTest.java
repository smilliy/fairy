package com.Hyperscale;

import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Date;
import java.util.Enumeration;
import java.util.Hashtable;
import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

import javax.swing.ButtonGroup;
import javax.swing.JOptionPane;


public class RunMainTest extends HyperscaleSensorTestTool implements Runnable, ActionListener{
	RunIpmiCmd runIpmiCmd = new RunIpmiCmd(this);
	boolean sensorTypeThreshold = true;
	Hashtable<String, String> sensorNameIDHashtable = new Hashtable<String, String>();
	Hashtable<String, String> sensorIDNameHashtable = new Hashtable<String, String>();
	Hashtable<String, String []> thresholdValueHashtable  = new Hashtable<String, String []>();
	Hashtable<String, String []> thresholdValueHashtable2  = new Hashtable<String, String []>(); //用来记录临时变量
	ArrayList<String> eventOffsetArrayList = new ArrayList<String>(); 
	ArrayList<String> eventstatusArrayList = new ArrayList<>();
	ArrayList<String> useridArrayList = new ArrayList<String>();
	ArrayList<String> passwordArrayList = new ArrayList<String>();
	ArrayList<String> ipArrayList = new ArrayList<>();
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		RunMainTest runMainTest = new RunMainTest();
		runMainTest.setVisible(true);
	}

	public RunMainTest() {
		new Thread(runIpmiCmd).start();
		runIpmiCmd.addcmd("ipmitool -V");
		textArea.setEditable(false);
		int width = Toolkit.getDefaultToolkit().getScreenSize().width;
		int height = Toolkit.getDefaultToolkit().getScreenSize().height;
		this.setLocation(width/2-this.getWidth()/2, height/2-this.getHeight()/2);
		this.btnNewButton_7.addActionListener(this);
		this.btnNewButton_7.setActionCommand("Refresh");
		this.btnNewButton_6.addActionListener(this);
		this.btnNewButton_6.setActionCommand("THD/DST");
		this.btnNewButton_5.addActionListener(this);
		this.btnNewButton_5.setActionCommand("Get SEL");
		this.btnNewButton_4.addActionListener(this);
		this.btnNewButton_4.setActionCommand("Clear RST");
		this.btnNewButton_3.addActionListener(this);
		this.btnNewButton_3.setActionCommand("Clear SEL");
		this.btnNewButton_2.addActionListener(this);
		this.btnNewButton_2.setActionCommand("Reset BMC");
		this.btnNewButton_1.addActionListener(this);
		this.btnNewButton_1.setActionCommand("DC Server");
		this.btnNewButton.addActionListener(this);
		this.btnNewButton.setActionCommand("Run Test");
		this.btnExeCmd.addActionListener(this);
		this.btnExeCmd.setActionCommand("Exe CMD");
		this.rdbtnNewRadioButton.addActionListener(this);
		this.rdbtnNewRadioButton.setActionCommand("Choose Sensor Name");
		this.rdbtnSensorId.addActionListener(this);
		this.rdbtnSensorId.setActionCommand("Choose Sensor ID");
		ButtonGroup bg = new ButtonGroup();
		bg.add(this.rdbtnNewRadioButton);
		bg.add(this.rdbtnSensorId);
		this.comboBox_4.addItemListener(new ItemListener() {
			
			@Override
			public void itemStateChanged(ItemEvent e) {
				// TODO Auto-generated method stub
				selectSensorName();
			}
		});
		//this.comboBox_4.setActionCommand("Select Sensor Name");
		this.comboBox_5.addItemListener(new ItemListener() {
			@Override
			public void itemStateChanged(ItemEvent e) {
				// TODO Auto-generated method stub
				if(e.getStateChange() == ItemEvent.SELECTED) {
					new Thread(new Runnable() {
						@Override
						public void run() {
							// TODO Auto-generated method stub
							selectSensorID();
						}
					}).start();
					
				}
			}
		});
		comboBox_5.removeAllItems();
		comboBox_4.removeAllItems();
		comboBox_5.setMaximumRowCount(15);
		comboBox_4.setMaximumRowCount(15);
		lblNewLabel_3.setToolTipText("这是更改iP后第一次获取的Sensor的阈值，供你更改为别的值后来参考。");
		this.comboBox.removeAllItems();
		this.comboBox.addItem("10.245.");
		this.comboBox.addItemListener(new ItemListener() {
			@Override
			public void itemStateChanged(ItemEvent e) {
				// TODO Auto-generated method stub
				if(e.getStateChange() == ItemEvent.SELECTED) {
					new Thread(new Runnable() {
						@Override
						public void run() {
							// TODO Auto-generated method stub
							String item = comboBox.getSelectedItem().toString();
							if(!ipArrayList.contains(item)) {
								ipArrayList.add(item);
								Collections.sort(ipArrayList);
								comboBox.removeAllItems();
								for(int i=0; i<ipArrayList.size(); i++) {
									comboBox.addItem(ipArrayList.get(i));
								}
							}
							comboBox.setSelectedItem(item);
						}
					}).start();
					
				}
			}
		});
		this.comboBox_1.removeAllItems();
		this.comboBox_1.addItem("USERID");
		this.comboBox_1.addItemListener(new ItemListener() {
			@Override
			public void itemStateChanged(ItemEvent e) {
				// TODO Auto-generated method stub
				if(e.getStateChange() == ItemEvent.SELECTED) {
					new Thread(new Runnable() {
						@Override
						public void run() {
							// TODO Auto-generated method stub
							String item = comboBox_1.getSelectedItem().toString();
							if(!useridArrayList.contains(item)) {
								useridArrayList.add(item);
								Collections.sort(useridArrayList);
								comboBox_1.removeAllItems();
								for(int i=0; i<useridArrayList.size(); i++) {
									comboBox_1.addItem(useridArrayList.get(i));
								}
							}
							comboBox_1.setSelectedItem(item);
						}
					}).start();
					
				}
			}
		});
		this.comboBox_2.removeAllItems();
		this.comboBox_2.addItem("PASSW0RD");
		this.comboBox_2.addItemListener(new ItemListener() {
			@Override
			public void itemStateChanged(ItemEvent e) {
				// TODO Auto-generated method stub
				if(e.getStateChange() == ItemEvent.SELECTED) {
					new Thread(new Runnable() {
						@Override
						public void run() {
							// TODO Auto-generated method stub
							String item = comboBox_2.getSelectedItem().toString();
							if(!passwordArrayList.contains(item)) {
								passwordArrayList.add(item);
								Collections.sort(passwordArrayList);
								comboBox_2.removeAllItems();
								for(int i=0; i<passwordArrayList.size(); i++) {
									comboBox_2.addItem(passwordArrayList.get(i));
								}
							}
							comboBox_2.setSelectedItem(item);
						}
					}).start();
					
				}
			}
		});
		//EventOffset的值
		this.comboBox_6.removeAllItems();
		String[]  eventoffsetStrings = {"Device Absent", "Device Present", "Device Disabled", "Presence detected", "Power Supply Failure detected", "Predictive Failure",
                "Power Supply AC lost", "State Asserted", "Thermal Trip", "Processor Presence detected", "Correctable ECC", "Uncorrectable ECC",
                "System Firmware Error", "Initiated by hard reset", "Initiated by warm reset",
                "Timer expired", "Hard Reset", "Power Down", "Power Cycle", "Timer interrupt", "Log Area Reset/Cleared"};
		for(int i=0; i<eventoffsetStrings.length; i++) {
			eventOffsetArrayList.add(eventoffsetStrings[i]);
		}
		Collections.sort(eventOffsetArrayList);
		for(int i=0; i<eventOffsetArrayList.size(); i++) {
			this.comboBox_6.addItem(eventOffsetArrayList.get(i));
		}
		this.comboBox_6.addItemListener(new ItemListener() {
			@Override
			public void itemStateChanged(ItemEvent e) {
				// TODO Auto-generated method stub
				if(e.getStateChange() == ItemEvent.SELECTED) {
					new Thread(new Runnable() {
						@Override
						public void run() {
							// TODO Auto-generated method stub
							String item = comboBox_6.getSelectedItem().toString();
							if(!eventOffsetArrayList.contains(item)) {
								eventOffsetArrayList.add(item);
								Collections.sort(eventOffsetArrayList);
								comboBox_6.removeAllItems();
								for(int i=0; i<eventOffsetArrayList.size(); i++) {
									comboBox_6.addItem(eventOffsetArrayList.get(i));
								}
							}
							comboBox_6.setSelectedItem(item);
						}
					}).start();
					
				}
			}
		});
		//事件状态
		this.comboBox_7.removeAllItems();
		eventstatusArrayList.add("assert");
		eventstatusArrayList.add("deassert");
		Collections.sort(eventstatusArrayList);
		for(int i=0; i<eventstatusArrayList.size(); i++) {
			this.comboBox_7.addItem(eventstatusArrayList.get(i));
		}
		this.comboBox_7.addItemListener(new ItemListener() {
			@Override
			public void itemStateChanged(ItemEvent e) {
				// TODO Auto-generated method stub
				if(e.getStateChange() == ItemEvent.SELECTED) {
					new Thread(new Runnable() {
						@Override
						public void run() {
							// TODO Auto-generated method stub
							String item = comboBox_7.getSelectedItem().toString();
							if(!eventstatusArrayList.contains(item)) {
								eventstatusArrayList.add(item);
								Collections.sort(eventstatusArrayList);
								comboBox_7.removeAllItems();
								for(int i=0; i<eventstatusArrayList.size(); i++) {
									comboBox_7.addItem(eventstatusArrayList.get(i));
								}
							}
							comboBox_7.setSelectedItem(item);
						}
					}).start();
					
				}
			}
		});
		
		
		
		
	}
	
	
	

	
	
	//检测系统中是否有ipmitool,并更改this中的文本信息
	class  RunIpmiCmd implements Runnable{
		RunMainTest rmt = null;
		Lock lock = new ReentrantLock();
		Lock lock1 = new ReentrantLock();
		Lock lock2 = new ReentrantLock();
		Thread thread1 = null;
		Thread thread2 = null;
		Queue<String> qquQueue = new LinkedList<String>();
	
		public RunIpmiCmd(RunMainTest rmt) {
			this.rmt = rmt;
		}
		
		public void addcmd(String cmdString) {
			qquQueue.offer(cmdString);
		}
		
		@Override
		public void run() {
			// TODO Auto-generated method stub
			while(true) {
				try {
					Thread.sleep(100);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				String cmdString = qquQueue.poll();
				if(cmdString!=null) {
					this.rmt.setTitle("Sensor Test Tool For Hyperscale -> 正在运行命令(还剩余"+ qquQueue.size() +"个)，请稍等。。。");
					SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");//设置日期格式
					rmt.textArea.append("\n[ "+df.format(new Date())+" ]\n"+cmdString+":\n");
					rmt.textArea.setCaretPosition(textArea.getText().length()); 
					runcmd2(cmdString);
					while(thread1.isAlive()&&thread2.isAlive()) {
						try {
							Thread.sleep(1000);
						} catch (InterruptedException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
						this.rmt.setTitle("Sensor Test Tool For Hyperscale -> 正在运行命令(还剩余"+ qquQueue.size() +"个)，请稍等。。。");
					}
				}else {
					SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");//设置日期格式
			        //System.out.println(df.format(new Date()));// new Date()为获取当前系统时间
					this.rmt.setTitle("Sensor Test Tool For Hyperscale (Version: 20180824) ->  " + df.format(new Date()));
				}
			}				
		}
		
		public void runcmd2(String cmdString) {
					
			Runtime rt = Runtime.getRuntime();
			Process p = null;
			try {
				p = rt.exec(cmdString);
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			InputStream in = p.getInputStream();
			InputStream inError = p.getErrorStream();
				
	
			//新建线程，处理调用CMD时返回错误信息
			thread1 = new Thread(new Runnable() {
				
				@Override
				public void run() {
					// TODO Auto-generated method stub
					lock1.lock();
					String line = null;
					BufferedReader bReaderE = new BufferedReader(new InputStreamReader(inError));
					try {
						while((line=bReaderE.readLine())!=null) {
							rmt.textArea.append(line+"\n");
							rmt.textArea.setCaretPosition(textArea.getText().length()); 
						}
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} finally {
						lock1.unlock();
					}
					
				}
			});
			thread1.start();
			
			//新建线程，处理调用CMD时返回信息
			thread2 = new Thread(new Runnable() {
				
				@Override
				public void run() {
					lock2.lock();
					// TODO Auto-generated method stub
					BufferedReader bReaderInfo = new BufferedReader(new InputStreamReader(in));
					String line = null;
					try {
						while((line=bReaderInfo.readLine())!=null) {
							rmt.textArea.append(line+"\n");
							rmt.textArea.setCaretPosition(textArea.getText().length()); 
						}
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} finally {
						lock2.unlock();
					}
					
				}
			});
			thread2.start();					
		}

	}


	@Override
	public void run() {
		// TODO Auto-generated method stub
		
	}
	
	

	public void clickSelLog() {
		// TODO Auto-generated method stub
		//JOptionPane.showOptionDialog(this, "aa", "bb");
		Object[] options = {" 确定 "," 取消 "};
		int response = JOptionPane.showOptionDialog(this, "是否获取SEL？", "Get SEL log。",JOptionPane.YES_OPTION, JOptionPane.QUESTION_MESSAGE, null, options, options[0]);  
		if(response == 0) {
			runIpmiCmd.addcmd("ipmitool -H "+ this.comboBox.getSelectedItem() +" -U "+ this.comboBox_1.getSelectedItem() +" -P "+ this.comboBox_2.getSelectedItem() +" -I "+ this.comboBox_3.getSelectedItem() + " sel list");
		}
	}
	
	public void clickClearResult() {
		Object[] options = {" 确定 "," 取消 "};
		int response = JOptionPane.showOptionDialog(this, "是否清空屏幕输出结果？", "Clear Test Result。",JOptionPane.YES_OPTION, JOptionPane.QUESTION_MESSAGE, null, options, options[0]);  
		if(response == 0) {
			this.textArea.setText("");
		}
	}
	
	public void clickClearSEL() {
		Object[] options = {" 确定 "," 取消 "};
		int response = JOptionPane.showOptionDialog(this, "是否清除SEL？", "Clear SEL log。",JOptionPane.YES_OPTION, JOptionPane.QUESTION_MESSAGE, null, options, options[0]);  
		if(response == 0) {
			runIpmiCmd.addcmd("ipmitool -H "+ this.comboBox.getSelectedItem() +" -U "+ this.comboBox_1.getSelectedItem() +" -P "+ this.comboBox_2.getSelectedItem() +" -I "+ this.comboBox_3.getSelectedItem() + " sel clear");
		}
	}
	
	public void clickResetBMC() {
		Object[] options = {" 确定 "," 取消 "};
		int response = JOptionPane.showOptionDialog(this, "是否重启BMC？", "Reset BMC。",JOptionPane.YES_OPTION, JOptionPane.QUESTION_MESSAGE, null, options, options[0]);  
		if(response == 0) {
			runIpmiCmd.addcmd("ipmitool -H "+ this.comboBox.getSelectedItem() +" -U "+ this.comboBox_1.getSelectedItem() +" -P "+ this.comboBox_2.getSelectedItem() +" -I "+ this.comboBox_3.getSelectedItem() + " raw 0x06 0x02");
		}
	}
	
	public void clickDCServer() {
		Object[] options = {" 确定 "," 取消 "};
		int response = JOptionPane.showOptionDialog(this, "是否重启机器？", "DC Server。",JOptionPane.YES_OPTION, JOptionPane.QUESTION_MESSAGE, null, options, options[0]);  
		if(response == 0) {
			runIpmiCmd.addcmd("ipmitool -H "+ this.comboBox.getSelectedItem() +" -U "+ this.comboBox_1.getSelectedItem() +" -P "+ this.comboBox_2.getSelectedItem() +" -I "+ this.comboBox_3.getSelectedItem() + " power cycle");
		}
	}
	
	public void clickExeCMD() {
		runIpmiCmd.addcmd("ipmitool -H "+ this.comboBox.getSelectedItem() +" -U "+ this.comboBox_1.getSelectedItem() +" -P "+ this.comboBox_2.getSelectedItem() +" -I "+ this.comboBox_3.getSelectedItem() + " " + this.txtRawxx.getText());
	}
	
	public void clickRunTest() {
		Object[] options = {" 确定 "," 取消 "};
		int response = JOptionPane.showOptionDialog(this, "是否开始测试？", "Run Test。",JOptionPane.YES_OPTION, JOptionPane.QUESTION_MESSAGE, null, options, options[0]);  
		if(response == 0) {
			if(sensorTypeThreshold) {
				this.textArea.append("\n开始Threshold sensor的测试：");
				this.textArea.setCaretPosition(textArea.getText().length()); 
//				String lncString = "0x" + thresholdValueHashtable2.get(comboBox_5.getSelectedItem().toString())[2];
//				String lcString = "0x" + thresholdValueHashtable2.get(comboBox_5.getSelectedItem().toString())[3];
//				String lcrString = "0x" + thresholdValueHashtable2.get(comboBox_5.getSelectedItem().toString())[4];
//				String uncString = "0x" + thresholdValueHashtable2.get(comboBox_5.getSelectedItem().toString())[5];
//				String ucString = "0x" + thresholdValueHashtable2.get(comboBox_5.getSelectedItem().toString())[6];
//				String ucrString = "0x" + thresholdValueHashtable2.get(comboBox_5.getSelectedItem().toString())[7];
//				if(!lncString.equals(txtx.getText().toString())) {
//					runIpmiCmd.addcmd("ipmitool -H "+ comboBox.getSelectedItem() +" -U "+ comboBox_1.getSelectedItem() +" -P "+ comboBox_2.getSelectedItem() +" -I "+ comboBox_3.getSelectedItem() + " -C 3 sensor thresh " + comboBox_4.getSelectedItem().toString() + " lnc "   );
//					System.out.println("kwwk");
//				}
//				if(!lcString.equals(txtx.getText().toString())) {
//					System.out.println("kwwk");
//				}
//				if(!lcrString.equals(txtx.getText().toString())) {
//					System.out.println("kwwk");
//				}
//				if(!uncString.equals(txtx.getText().toString())) {
//					System.out.println("kwwk");
//				}
//				if(!ucString.equals(txtx.getText().toString())) {
//					System.out.println("kwwk");
//				}
//				if(!ucrString.equals(txtx.getText().toString())) {
//					System.out.println("kwwk");
//				}
				
				runIpmiCmd.addcmd("ipmitool -H "+ comboBox.getSelectedItem() +" -U "+ comboBox_1.getSelectedItem() +" -P "+ comboBox_2.getSelectedItem() +" -I "+ comboBox_3.getSelectedItem() + 
						" raw 0x04 0x26 " + comboBox_5.getSelectedItem().toString() + " 0x" + thresholdValueHashtable.get(comboBox_4.getSelectedItem().toString()) + " " + txtx.getText() + " " + 
						txtx_2.getText() + " " + txtx_4.getText() + " " + txtx_1.getText() +" " + txtx_3.getText() +" " + txtx_5.getText() );
			}else {
				this.textArea.append("\n开始Discrete sensor的测试：");
				this.textArea.setCaretPosition(textArea.getText().length()); 
				runIpmiCmd.addcmd("ipmitool -H "+ comboBox.getSelectedItem() +" -U "+ comboBox_1.getSelectedItem() +" -P "+ comboBox_2.getSelectedItem() +" -I "+ comboBox_3.getSelectedItem() +
						" event \"" + comboBox_4.getSelectedItem().toString() + "\" \"" + comboBox_6.getSelectedItem().toString() + "\" " + comboBox_7.getSelectedItem().toString());
			}
		}
	}
	
	public void showThreshold() {
		this.contentPane.remove(panel_3);
		contentPane.add(panel_2);
		panel_2.setBounds(10, 210, 600, 122);
		this.btnNewButton_6.setText("DST/THD");
		this.repaint();
		this.setVisible(true);
	}
	
	public void showDiscrete() {
		this.contentPane.remove(panel_2);
		contentPane.add(panel_3);
		panel_3.setBounds(10, 210, 600, 122);
		this.btnNewButton_6.setText("THD/DST");
		this.repaint();
		this.setVisible(true);
	}
	
	public void clickTHD_DST() {
		if(!sensorTypeThreshold){
			sensorTypeThreshold = true;
			showThreshold();
		}else{
			sensorTypeThreshold = false;
			showDiscrete();
		}
	}
	
	public void chooseSensorName() {
		this.comboBox_4.removeAllItems();
		this.comboBox_5.removeAllItems();
		sensorNameIDHashtable.clear();
		sensorIDNameHashtable.clear();
		//this.setTitle("Sensor Test Tool For Hyperscale -> 正在获取Sensor Name和SensorID, 请稍等...");
		this.textArea.append("\n正在获取Sensor Name和SensorID, 请稍等...\n");
		this.textArea.setCaretPosition(textArea.getText().length()); 
		//runIpmiCmd.addcmd("ipmitool -H "+ this.comboBox.getSelectedItem() +" -U "+ this.comboBox_1.getSelectedItem() +" -P "+ this.comboBox_2.getSelectedItem() +" -I "+ this.comboBox_3.getSelectedItem() + " sdr list");
		new Thread(new Runnable() {
			
			@Override
			public void run() {
				// TODO Auto-generated method stub
				Runtime rt = Runtime.getRuntime();
				Process p = null;
				try {
					p = rt.exec("ipmitool -H "+ comboBox.getSelectedItem() +" -U "+ comboBox_1.getSelectedItem() +" -P "+ comboBox_2.getSelectedItem() +" -I "+ comboBox_3.getSelectedItem() + " sdr elist");
				} catch (IOException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				InputStream in = p.getInputStream();
				InputStream inError = p.getErrorStream();
					
		
				//新建线程，处理调用CMD时返回错误信息
				Thread thread1 = new Thread(new Runnable() {
					
					@Override
					public void run() {
						// TODO Auto-generated method stub
					
						String line = null;
						BufferedReader bReaderE = new BufferedReader(new InputStreamReader(inError));
						try {
							while((line=bReaderE.readLine())!=null) {
								textArea.append("\n"+line);
								textArea.setCaretPosition(textArea.getText().length()); 
							}
						} catch (IOException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						} finally {
							
						}
						
					}
				});
				thread1.start();
				//新建线程，处理调用CMD时返回信息
				Thread thread2 = new Thread(new Runnable() {
					
					@Override
					public void run() {
						// TODO Auto-generated method stub
						BufferedReader bReaderInfo = new BufferedReader(new InputStreamReader(in));
						String line = null;
						try {
							textArea.append("\n"+"ipmitool -H "+ comboBox.getSelectedItem() +" -U "+ comboBox_1.getSelectedItem() +" -P "+ comboBox_2.getSelectedItem() +" -I "+ comboBox_3.getSelectedItem() + " sdr elist"+"\n");
							while((line=bReaderInfo.readLine())!=null) {
								textArea.append("\n"+line);
								sensorNameIDHashtable.put(line.split("\\|")[0].trim(), "0x"+line.split("\\|")[1].trim().substring(0, 2));
								sensorIDNameHashtable.put("0x"+line.split("\\|")[1].trim().substring(0, 2), line.split("\\|")[0].trim());
								textArea.setCaretPosition(textArea.getText().length()); 
							}
						} catch (Exception e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						} finally {
						}
						
						Enumeration<String> key = sensorNameIDHashtable.keys();
						ArrayList<String> arrayList1 = new ArrayList<String>();
						while(key.hasMoreElements()) {
							arrayList1.add(key.nextElement());
						}
						Collections.sort(arrayList1);
						for(int i=0; i<arrayList1.size(); i++) {
							comboBox_4.addItem(arrayList1.get(i));
						}
						
						Enumeration<String> key2 = sensorIDNameHashtable.keys();
						ArrayList<String> arrayList2 = new ArrayList<String>();
						while(key2.hasMoreElements()) {
							arrayList2.add(key2.nextElement());
						}
						Collections.sort(arrayList2);
						for(int i=0; i<arrayList2.size(); i++) {
							comboBox_5.addItem(arrayList2.get(i));
						}
						
						try {
							comboBox_4.setSelectedItem(arrayList1.get(0));
							comboBox_5.setSelectedItem(sensorNameIDHashtable.get(arrayList1.get(0)));
						} catch (Exception e2) {
							// TODO: handle exception
						}
						

					}
				});
				thread2.start();	
				int i=0;
				while(true) {
					if(thread1.isAlive()||thread2.isAlive()) {
						i++;
						if(i<20) {
							textArea.append("..");
							textArea.setCaretPosition(textArea.getText().length());
						}else {
							i=0;
						}
						try {
							Thread.sleep(200);
						} catch (InterruptedException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
					}else {
						textArea.append("\nSensor Name和SensorID获取完成。\n");
						textArea.setCaretPosition(textArea.getText().length());
						break;
					}
				}
			}
		}).start();
	}
	
	public void chooseSensorID() {
		chooseSensorName();
	}
	
	

	
	public void selectSensorName() {
		try {
			comboBox_5.setSelectedItem(sensorNameIDHashtable.get(comboBox_4.getSelectedItem()).toString());
			//System.out.println(sensorNameIDHashtable.get(comboBox_4.getSelectedItem()).toString());
		} catch (Exception e) {
			// TODO: handle exception
			e.getStackTrace();
		}	
		//new Thread(new CheckThresholdDiscreteSensor(this, sensorNameIDHashtable.get(comboBox_4.getSelectedItem()))).start();
		
	}
	
	
	public void clickRefresh() {
		try {
			comboBox_4.setSelectedItem(sensorIDNameHashtable.get(comboBox_5.getSelectedItem()).toString());
			new Thread(new Runnable() {
				
				@Override
				public void run() {
					// TODO Auto-generated method stub
					try {
						//System.out.println("ipmitool -H "+ comboBox.getSelectedItem() +" -U "+ comboBox_1.getSelectedItem() +" -P "+ comboBox_2.getSelectedItem() +" -I "+ comboBox_3.getSelectedItem() + " raw 0x04 0x27 " + comboBox_5.getSelectedItem().toString());
						Process process = Runtime.getRuntime().exec("ipmitool -H "+ comboBox.getSelectedItem() +" -U "+ comboBox_1.getSelectedItem() +" -P "+ comboBox_2.getSelectedItem() +" -I "+ comboBox_3.getSelectedItem() + " raw 0x04 0x27 " + comboBox_5.getSelectedItem().toString());
						new Thread(new Runnable() {
							
							@Override
							public void run() {
								// TODO Auto-generated method stub
								BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(process.getInputStream()));
								try {
									String line = "";
									while((line=bufferedReader.readLine())!=null) {
										//textArea.append(line+"\n");
										//textArea.setCaretPosition(textArea.getText().length()); 
										sensorTypeThreshold = true;
										showThreshold();
										if(!thresholdValueHashtable.containsKey(comboBox_5.getSelectedItem().toString())) {
											thresholdValueHashtable.put(comboBox_5.getSelectedItem().toString(), line.split(" "));
											lblNewLabel_3.setText("(LNC: 0x"+line.split(" ")[2] +",  LC: 0x"+line.split(" ")[3]+",  LCR: 0x"+line.split(" ")[4]+",  UNC: 0x"+line.split(" ")[5]+",  UC: 0x"+line.split(" ")[6]+",  UCR: 0x"+line.split(" ")[7]);
										}else {
											lblNewLabel_3.setText("(LNC: 0x"+line.split(" ")[2] +",  LC: 0x"+line.split(" ")[3]+",  LCR: 0x"+line.split(" ")[4]+",  UNC: 0x"+line.split(" ")[5]+",  UC: 0x"+line.split(" ")[6]+",  UCR: 0x"+line.split(" ")[7]);
										}
//										for(int i=0; i<thresholdValueHashtable.get(comboBox_5.getSelectedItem().toString()).length; i++) {
//											System.out.println(thresholdValueHashtable.get(comboBox_5.getSelectedItem().toString())[i]);
//										}
										thresholdValueHashtable2.put(comboBox_5.getSelectedItem().toString(), line.split(" "));
										txtx.setText("0x"+line.split(" ")[2]);
										txtx_2.setText("0x"+line.split(" ")[3]);
										txtx_4.setText("0x"+line.split(" ")[4]);
										txtx_1.setText("0x"+line.split(" ")[5]);
										txtx_3.setText("0x"+line.split(" ")[6]);
										txtx_5.setText("0x"+line.split(" ")[7]);
										
									}
								} catch (Exception e) {
									// TODO Auto-generated catch block
									e.printStackTrace();
								}
							}
						}).start();
						
						new Thread(new Runnable() {
							
							@Override
							public void run() {
								// TODO Auto-generated method stub
								BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(process.getErrorStream()));
								try {
									String line = "";
									while((line=bufferedReader.readLine())!=null) {
										//textArea.append(line+"\n");
										//textArea.setCaretPosition(textArea.getText().length()); 
										sensorTypeThreshold = false;
										showDiscrete();
										txtx.setText("0x00");
										txtx_2.setText("0x00");
										txtx_4.setText("0x00");
										txtx_1.setText("0x00");
										txtx_3.setText("0x00");
										txtx_5.setText("0x00");
										lblNewLabel_6.setText("0x00");
										lblNewLabel_3.setText("(LNC: 0x00,  LC: 0x00,  LCR: 0x00,  UNC: 0x00,  UC: 0x00,  UCR: 0x00)");
									}
								} catch (IOException e) {
									// TODO Auto-generated catch block
									e.printStackTrace();
								}
							}
						}).start();
					
					
					
					} catch (Exception e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
			}).start();
		} catch (Exception e) {
			// TODO: handle exception
			e.getStackTrace();
		}	
		
		try {
			comboBox_4.setSelectedItem(sensorIDNameHashtable.get(comboBox_5.getSelectedItem()).toString());
			new Thread(new Runnable() {
				
				@Override
				public void run() {
					// TODO Auto-generated method stub
					try {
						//System.out.println("ipmitool -H "+ comboBox.getSelectedItem() +" -U "+ comboBox_1.getSelectedItem() +" -P "+ comboBox_2.getSelectedItem() +" -I "+ comboBox_3.getSelectedItem() + " raw 0x04 0x2d " + comboBox_5.getSelectedItem().toString());
						Process process2 = Runtime.getRuntime().exec("ipmitool -H "+ comboBox.getSelectedItem() +" -U "+ comboBox_1.getSelectedItem() +" -P "+ comboBox_2.getSelectedItem() +" -I "+ comboBox_3.getSelectedItem() + " raw 0x04 0x2d " + comboBox_5.getSelectedItem().toString());
						new Thread(new Runnable() {
							
							@Override
							public void run() {
								// TODO Auto-generated method stub
								BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(process2.getInputStream()));
								try {
									String line = "";
									while((line=bufferedReader.readLine())!=null) {
										//textArea.append(line+"\n");
										//textArea.setCaretPosition(textArea.getText().length()); 
										lblNewLabel_6.setText("0x"+line.split(" ")[1]);
									}
								} catch (Exception e) {
									// TODO Auto-generated catch block
									e.printStackTrace();
								}
							}
						}).start();
						
						new Thread(new Runnable() {
							
							@Override
							public void run() {
								// TODO Auto-generated method stub
								BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(process2.getErrorStream()));
								try {
									String line = "";
									while((line=bufferedReader.readLine())!=null) {
										textArea.append(line+"\n");
										textArea.setCaretPosition(textArea.getText().length()); 
									}
								} catch (IOException e) {
									// TODO Auto-generated catch block
									e.printStackTrace();
								}
							}
						}).start();
					
					
					
					} catch (Exception e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
			}).start();
		} catch (Exception e) {
			// TODO: handle exception
			e.getStackTrace();
		}	
	}
	
	public void selectSensorID() {
		clickRefresh();
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getActionCommand().equals("Get SEL")) {
			new Thread(new Runnable() {
				
				@Override
				public void run() {
					// TODO Auto-generated method stub
					clickSelLog();
				}
			}).start();
		}
		
		if(e.getActionCommand().equals("Clear RST")) {
			new Thread(new Runnable() {
				
				@Override
				public void run() {
					// TODO Auto-generated method stub
					clickClearResult();
				}
			}).start();
		}
		
		if(e.getActionCommand().equals("Clear SEL")) {
			new Thread(new Runnable() {
				
				@Override
				public void run() {
					// TODO Auto-generated method stub
					clickClearSEL();
				}
			}).start();
		}
		
		if(e.getActionCommand().equals("Reset BMC")) {
			new Thread(new Runnable() {
				
				@Override
				public void run() {
					// TODO Auto-generated method stub
					clickResetBMC();
				}
			}).start();
		}
	
		if(e.getActionCommand().equals("DC Server")) {
			new Thread(new Runnable() {
				
				@Override
				public void run() {
					// TODO Auto-generated method stub
					clickDCServer();
				}
			}).start();
		}
		
		if(e.getActionCommand().equals("Exe CMD")) {
			new Thread(new Runnable() {
				
				@Override
				public void run() {
					// TODO Auto-generated method stub
					clickExeCMD();
				}
			}).start();
		}
		
		if(e.getActionCommand().equals("THD/DST")) {
			new Thread(new Runnable() {
				
				@Override
				public void run() {
					// TODO Auto-generated method stub
					clickTHD_DST();
				}
			}).start();
		}
		
		if(e.getActionCommand().equals("Run Test")) {
			new Thread(new Runnable() {
				
				@Override
				public void run() {
					// TODO Auto-generated method stub
					clickRunTest();
				}
			}).start();
		}
		
		if(e.getActionCommand().equals("Choose Sensor Name")) {
			new Thread(new Runnable() {
				
				@Override
				public void run() {
					// TODO Auto-generated method stub
					chooseSensorName();
				}
			}).start();
		}
		
		if(e.getActionCommand().equals("Choose Sensor ID")) {
			new Thread(new Runnable() {
				
				@Override
				public void run() {
					// TODO Auto-generated method stub
					chooseSensorID();
				}
			}).start();
		}
		

		if(e.getActionCommand().equals("Refresh")) {
			new Thread(new Runnable() {
				
				@Override
				public void run() {
					// TODO Auto-generated method stub
					try {
						runIpmiCmd.addcmd("ipmitool -H "+ comboBox.getSelectedItem() +" -U "+ comboBox_1.getSelectedItem() +" -P "+ comboBox_2.getSelectedItem() +" -I "+ comboBox_3.getSelectedItem() + " raw 0x04 0x27 " + comboBox_5.getSelectedItem().toString());
						runIpmiCmd.addcmd("ipmitool -H "+ comboBox.getSelectedItem() +" -U "+ comboBox_1.getSelectedItem() +" -P "+ comboBox_2.getSelectedItem() +" -I "+ comboBox_3.getSelectedItem() + " raw 0x04 0x2d " + comboBox_5.getSelectedItem().toString());
						clickRefresh();
					} catch (Exception e2) {
						// TODO: handle exception
					}

				}
			}).start();
		}
		
		
	}
}
